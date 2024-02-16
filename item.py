from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., description="The name of the item", x_custom_other_field="Custom value for name", juan="HOLA")
    description: str = Field(None, description="The description of the item", extra={"x-custom-other-field": "Custom value for descripton", "juan": "HOLA"})