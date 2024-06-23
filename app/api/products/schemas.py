from pydantic import BaseModel

from app.utils.base_schemas import BaseAuditDTOSchema, BaseAuditModelSchema


class ProductSchema(BaseAuditDTOSchema):

    display_name: str
    name: str
    description: str
    value: float
    available: bool



class ProductPublic(ProductSchema, BaseAuditModelSchema):
    id: int
    display_name: str
    name: str
    description: str
    value: float
    available: bool



class ProductListSchema(BaseModel):
    Product: list[ProductSchema]
