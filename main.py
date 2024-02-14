from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()

# Define your API routes here
@app.get("/items/")
async def read_items():
    return [{"name": "Foo"}]

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version="2.5.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    # Add custom x- field at the root of the schema
    openapi_schema["x-custom-field"] = "value"
    # You can also add custom x- fields in other parts of the schema,
    # for example, within a path object
    openapi_schema["paths"]["/items/"]["get"]["x-custom-operation-field"] = "value"
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Run the app with:
# uvicorn main:app --reload