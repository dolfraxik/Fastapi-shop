from pydantic import BaseModel , Field # type: ignore
import datetime
from decimal import Decimal 
from typing import Optional
from .category import CategoryResponse

class ProductBase(BaseModel):
    name: str = Field(... ,min_length=2, max_length=80, description='Enter the name product')
    description: Optional[str] = Field(None,description='Clean URL the category name')
    price : Decimal = Field(..., max_digits=10, gt=0,decimal_places=2, description='Price product')
    category_id: int = Field(..., description='Category id')
    image_url: Optional[str] = Field(None,description='Product image URL')

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int = Field(..., description='id product')
    description: Optional[str]
    price : Decimal
    category_id: int
    image_url: Optional[str]
    created_at: datetime
    category: CategoryResponse = Field(..., description='product category details')

    class Config:
        from_attributes= True

class ProductListResponse(ProductBase):
    pruducts: list[ProductResponse]
    total: int = Field(..., description = 'Total number of products')