from sqlalchemy.orm import Session # type: ignore
from typing import List
from ..repositories.category_repository import CategoryRepository
from ..schemas.category import CategoryResponse, CategoryCreate
from fastapi import HTTPException, status # type: ignore

class CategoryServices:
    def __init__(self, db: Session):
        self.repository = CategoryRepository(db)

    def get_all_categories(self) -> List[CategoryResponse]:
        categories = self.repository.get_all()
        return [CategoryResponse.model_validate(cat) for cat in categories]
    
    def get_by_id_category(self, category_id: int) -> CategoryRepository:
        category = self.repository.get_by_id(category_id)
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Not found {category_id}')
        return CategoryResponse.model_validate(category)
    
    def create_category(self,category_data: CategoryCreate)-> CategoryResponse:
        create_category = self.reposirory.create(category_data)
        return CategoryResponse.model_validate(create_category)
       
