from fastapi import FastAPI
from x_field import x_field, create_openapi
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

app.openapi = create_openapi(app)

# Run the app with:
# uvicorn main:app --reload

# get the openapi schema with:
# curl -X 'GET' 'http://localhost:8000/openapi.json'

