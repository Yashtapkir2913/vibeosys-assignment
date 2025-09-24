from pydantic import BaseModel
from typing import Optional
from models import CategoryEnum, UnitEnum

class ProductBase(BaseModel):
    name: str
    category: CategoryEnum
    description: Optional[str]
    product_image: Optional[str]
    sku: Optional[str]
    unit_of_measure: Optional[UnitEnum]
    lead_time: Optional[int]

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductInfo(ProductBase):
    id: int
    class Config:
        orm_mode = True
