from sqlalchemy.orm import Session # type: ignore
from typing import List
from ..repositories.product_repository import ProductRepository
from ..repositories.category_repository import CategoryRepository
from ..schemas.product import ProductResponse, ProductCreate, ProductListResponse
from fastapi import HTTPException, status # type: ignore

class ProductServices:
    def __init__(self, db: Session):
        self.product_repo = ProductRepository(db)
        self.category_repo = CategoryRepository(db)

    def get_all_products(self) -> ProductListResponse:
        products = self.product_repo.get_all()
        products_response = [ProductResponse.model_validate(prod) for prod in products]
        
        return ProductListResponse(
            products=products_response, 
            total=len(products_response)
        )

    def get_by_id_product(self, product_id: int) -> ProductResponse:
        product = self.product_repo.get_by_id(product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Product not found with id {product_id}'
            )
        
        return ProductResponse.model_validate(product)
    
    
    def get_products_by_category(self, category_id: int) -> ProductListResponse:
        category = self.category_repository.get_by_id(category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Category with id {category_id} not found"
            )
        
        products = self.product_repository.get_by_category(category_id)
        products_response = [ProductResponse.model_validate(prod) for prod in products]
        
        return ProductListResponse(
            products=products_response, 
            total=len(products_response)
        )
    
    def create_product(self, product_data: ProductCreate) -> ProductResponse:
        category = self.category_repo.get_by_id(product_data.category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Category with id {product_data.category_id} does not exist"
            )
            
        product = self.product_repo.create(product_data)
        return ProductResponse.model_validate(product)