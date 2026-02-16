from sqlalchemy import select # type: ignore
from sqlalchemy.orm import Session # type: ignore
from typing import List, Optional 
from ..models.category import Category
from ..schemas.category import CategoryCreate

class CategoryReposity:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Category]:
        request = select(Category)
        result = self.db.execute(request)
        return result.scalars().all() 

    
    def get_by_id(self, category_id:int) -> Optional[Category]:
        query = select(Category).where(Category.id_category == category_id)
        result = self.db.execute(query)
        return result.scalar_one_or_none()

    def get_by_slug(self, slug:str) -> Optional[Category]:
        query = select(Category).where(Category.slug == slug)
        result = self.db.execute(query)
        return result.scalar_one_or_none()
    
    def create(self, category_data: CategoryCreate) -> Category:
        db_category = Category(**category_data.model_dump())
        self.db.add(db_category)
        self.db.commit()
        self.refresh(db_category)
        return db_category
