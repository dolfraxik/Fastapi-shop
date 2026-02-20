from sqlalchemy.orm import Session # type: ignore
from typing import Dict
from ..repositories.product_repository import ProductRepository
from ..schemas.cart import CartResponse, CartItem, CartItemCreate, CartItemUpdate
from fastapi import HTTPException, status # type: ignore

class CartService:
    def __init__(self, db: Session):
        self.product_repo = ProductRepository(db)

    def add_to_cart(self, cart_data: Dict[int, int], item: CartItemCreate) -> Dict[int, int]:
        product = self.product_repo.get_by_id(item.product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Product with id {item.product_id} not found'
            )

        cart_data[item.product_id] = cart_data.get(item.product_id, 0) + item.quantity
        return cart_data

    def update_cart_item(self, cart_data: Dict[int, int], item: CartItemUpdate) -> Dict[int, int]:
        if item.product_id not in cart_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found in cart"
            )
        cart_data[item.product_id] = item.quantity
        return cart_data

    def remove_from_cart(self, cart_data: Dict[int, int], product_id: int) -> Dict[int, int]:
        if product_id not in cart_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not in cart")
        del cart_data[product_id]
        return cart_data

    def get_cart_details(self, cart_data: Dict[int, int]) -> CartResponse:
        if not cart_data:
            return CartResponse(items=[], total=0.0, items_count=0)

        products = self.product_repo.get_multiple_by_ids(list(cart_data.keys()))
        products_dict = {p.id_product: p for p in products}

        cart_items = []
        total_price = 0.0
        total_items = 0

        for p_id, qty in cart_data.items():
            if p_id in products_dict:
                p = products_dict[p_id]
                subtotal = p.price * qty
                cart_items.append(CartItem(
                    product_id=p.id_product, name=p.name, price=p.price,
                    quantity=qty, subtotal=subtotal, image_url=p.image_url
                ))
                total_price += subtotal
                total_items += qty

        return CartResponse(items=cart_items, total=total_price, items_count=total_items)