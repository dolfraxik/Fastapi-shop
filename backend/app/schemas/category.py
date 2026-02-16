from pydantic import BaseModel, Field                          # type: ignore

class CategoryBase(BaseModel):
    name: str = Field(... ,min_length=2, max_length=80, description='Enter the name product')
    slug: str = Field(...,min_length=1, max_length=63,description='Clean URL the category name')

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int = Field(..., description='unique category identifier')

    class Config:
        from_attributes= True