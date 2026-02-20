from sqlalchemy import select # type: ignore
from sqlalchemy.orm import Session, joinedload # type: ignore
from typing import List, Optional 
from ..models.product import Product
from ..schemas.product import ProductCreate

class ProductRepository:
    def __init__(self, db:Session):
        self.db = db

    def get_all(self)-> List[Product]:
        query = select(Product).options(joinedload(Product.category))
        result = self.db.execute(query)
        return result.scalars().all()
    
    def get_by_id(self, product_id: int) -> Optional[Product]:
        query = select(Product).where(Product.id_product == product_id).options(joinedload(Product.category))
        result = self.db.execute(query)
        return result.scalar_one_or_none()
    
    def get_by_category(self, category_id: int) -> List[Product]:
        query = select(Product).where(Product.category_id == category_id).options(joinedload(Product.category))
        result = self.db.execute(query)
        return result.scalars().all() 

    def create(self, product_data: ProductCreate) -> Product:
        db_product = Product(**product_data.model_dump())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product) 
        return db_product 

    def get_multiple_by_ids(self, product_ids: List[int]) -> List[Product]:
        query = select(Product).where(Product.id_product.in_(product_ids)).options(joinedload(Product.category))
        result = self.db.execute(query)
        return result.scalars().all()