import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship # type: ignore
from database import Base
from sqlalchemy import DateTime ,ForeignKey# type: ignore
class Product(Base):
    __tablename__ = 'products'

    id_product: Mapped[int] = mapped_column(primary_key=True, index=True)
    product_name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str]
    price: Mapped[float] = mapped_column(nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)
    image_url: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    
    category = relationship("Category", back_populates="products")

    
    def summary(self):
        return f'<Product{self.id_product}, name={self.product_name}, price={self.price}>'
    