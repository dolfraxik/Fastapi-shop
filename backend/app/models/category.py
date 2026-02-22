from sqlalchemy.orm import Mapped, mapped_column, relationship # type: ignore
from ..database import Base

class Category(Base):
    __tablename__ = 'categories'

    id_category: Mapped[int] = mapped_column(primary_key=True,index= True)
    name: Mapped[str] = mapped_column(unique=True,nullable=False, index = True)
    slug: Mapped[str] = mapped_column(unique=True,nullable=False, index = True)

    products = relationship('Product', back_populates='category')

    def __repr__(self):
        return f'<Category(id={self.id}, name={self.name})>'