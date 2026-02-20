from sqlalchemy.orm import Session # type: ignore

from ..repositories.product_repository import ProductRepository
from ..repositories.category_repository import CategoryRepository
from ..schemas.product import ProductResponse, ProductCreate, ProductListResponse
from fastapi import HTTPException, status # type: ignore

class ProductService:
    def __init__(self, db: Session):
        self.product_repo = ProductRepository(db)
        self.category_repo = CategoryRepository(db)

    def get_all_products(self) -> ProductListResponse:
        products = self.product_repo.get_all()
        items = [ProductResponse.model_validate(p) for p in products]
        return ProductListResponse(products=items, total=len(items))

    def get_by_id_product(self, product_id: int) -> ProductResponse:
        product = self.product_repo.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
        return ProductResponse.model_validate(product)
    
    def get_products_by_category(self, category_id: int) -> ProductListResponse:
        if not self.category_repo.get_by_id(category_id):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
        
        products = self.product_repo.get_by_category(category_id)
        items = [ProductResponse.model_validate(p) for p in products]
        return ProductListResponse(products=items, total=len(items))
    
    def create_product(self, product_data: ProductCreate) -> ProductResponse:
        if not self.category_repo.get_by_id(product_data.category_id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid category")
            
        product = self.product_repo.create(product_data)
        return ProductResponse.model_validate(product)