import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

class Product(Base):
    __tablename__ = 'products'

    id_product: Mapped[int] = mapped_column(primary_key=True, index=True)
    product_name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str]
    price: Mapped[float] = mapped_column(nullable=False)
    amount: Mapped[int] = mapped_column(unique=True,nullable=False)
    image_url: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),nullable=False)
    
    categories = relationship('Category', back_populates = 'category')
    
    def summary(self):
        return f'<Product{self.id_product}, name={self.product_name}, price={self.price}>'
    