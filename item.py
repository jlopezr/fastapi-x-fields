from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., description="The name of the item")
    description: str = Field(None, description="The description of the item")

    class Config:
        json_schema_extra = {
            "properties": {
                "name": {
                    "x-custom-field": "Custom value for name"
                },
                "description": {
                    "x-custom-field": "Custom value for description"
                },
            }
        }