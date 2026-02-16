from pydantic import BaseModel, Field # type: ignore
from typing import Optional

# Базовая модель для элемента корзины
class CartItemBase(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="Quantity (must be greater than 0)")

# Схема для добавления товара (наследует базу)
class CartItemCreate(CartItemBase):
    pass

# Схема для обновления количества товара
class CartItemUpdate(BaseModel):
    product_id: int = Field(..., description="Product ID")
    quantity: int = Field(..., gt=0, description="New quantity (must be greater than 0)")

# Схема для отображения товара в корзине (с полной информацией)
class CartItem(BaseModel):
    product_id: int
    name: str = Field(..., description="Product name")
    price: float = Field(..., description="Product price")
    quantity: int = Field(..., description="Quantity in cart")
    subtotal: float = Field(..., description="Total price for this item (price * quantity)")
    image_url: Optional[str] = Field(None, description="Product image URL")

class CartResponse(BaseModel):
    items: list[CartItem] = Field(..., description="List of items in cart")
    total: float = Field(..., description="Total cart price")
    items_count: int = Field(..., description="Total number of items in cart")