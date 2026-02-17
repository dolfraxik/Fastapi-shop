from fastapi import APIRouter, Depends, status # type: ignore
from sqlalchemy.orm import Session # type: ignore
from typing import List
from ..database import get_db
from ..services.category_service import CategoryService # type: ignore
from ..schemas.category import CategoryResponse

router = APIRouter(
    prefix='/api/categories',
    tags=['caregories']
)

@router.get('', response_model=List[CategoryResponse], status_code=status.HTTP_200_OK)
async def get_categories(session: Session = Depends(get_db)):
    service = CategoryService(session)
    return service.get_all_categories(session)

@router.get('{category_id}', response_model=CategoryResponse, status=status.HTTP_200_Ok)
async def get_by_id( category_id: int,session: Session = Depends(get_db)):
    service = CategoryService( session)
    return service.get_category_by_id(category_id)

