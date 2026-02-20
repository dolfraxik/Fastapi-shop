from pydantic import BaseModel , Field # type: ignore
from datetime import datetime
from decimal import Decimal 
from typing import List, Optional
from .category import CategoryResponse

class ProductBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=80, description='Product name')
    description: Optional[str] = Field(None, description='Product description')
    price: Decimal = Field(..., max_digits=10, decimal_places=2, gt=0, description='Product price')
    category_id: int = Field(..., description='Category ID')
    image_url: Optional[str] = Field(None, description='Product image URL')

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id_product: int = Field(..., description='Unique product identifier')
    created_at: datetime
    category: CategoryResponse = Field(..., description='Product category details')

    class Config:
        from_attributes = True

class ProductListResponse(BaseModel): 
    products: List[ProductResponse] 
    total: int = Field(..., description='Total number of products')