from fastapi import APIRouter, Depends, status # type: ignore
from sqlalchemy.orm import Session # type: ignore
from typing import List
from ..database import get_db
from ..services.product_service import ProductService  
from ..schemas.product import ProductResponse, ProductListResponse

router = APIRouter(
    prefix='/api/products',
    tags=['products']
)

@router.get('', response_model=List[ProductListResponse], status_code=status.HTTP_200_OK)
async def get_products(session: Session = Depends(get_db)):
    service = ProductService(session)
    return service.get_all_products(session)

@router.get('/{product_id}', response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def get_by_id(product_id: int,session: Session = Depends(get_db)):
    service = ProductService( session)
    return service.get_by_id_product(product_id)

@router.get("/category/{category_id}", response_model=ProductListResponse, status_code=status.HTTP_200_OK)
def get_products_by_category(category_id: int, db: Session = Depends(get_db)):
    service = ProductService(db)
    return service.get_products_by_category(category_id)
