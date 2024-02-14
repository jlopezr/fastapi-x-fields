from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from x_field import x_field
from item import Item

app = FastAPI()

# Define your API routes here
@app.get("/items/")
@x_field(x_example="Example GET", x_description="An example x-field for demons")
async def read_items():
    return [{"name": "Foo"}]

@app.get("/items2/")
async def read_items2():
    return [{"name": "Foo"}]

@app.post("/items/")
@x_field(x_example="Example POST", x_description="An example x-field for demons")
async def post_items(item: Item):
    return [{"name": "Foo"}]

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="1.0.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )

    for route in app.routes:
        if hasattr(route, "endpoint") and hasattr(route.endpoint, "x_fields"):
            x_fields = getattr(route.endpoint, "x_fields")
            # Identify the route's operations in the OpenAPI schema
            for method in route.methods:
                # Normalize HTTP method to lowercase
                method_lower = method.lower()
                # Access the route in OpenAPI schema if it exists
                if route.path in openapi_schema["paths"] and method_lower in openapi_schema["paths"][route.path]:
                    operation = openapi_schema["paths"][route.path][method_lower]
                    # Apply x_fields to the operation
                    operation.update(x_fields)

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Run the app with:
# uvicorn main:app --reload

# get the openapi schema with:
# curl -X 'GET' 'http://localhost:8000/openapi.json'

