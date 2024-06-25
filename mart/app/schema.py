from sqlmodel import SQLModel, Field
from uuid import UUID, uuid4
from typing import Optional

class BaseProduct(SQLModel):
    name: str
    category: str = Field(default='food | health | fashion | electronics | sports | vahicle | furniture | literature | other')
    price: int
    quantity : int

class Product(BaseProduct, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)

class ProductReq(BaseProduct):
    pass

class UpdateProduct(SQLModel):
    name: Optional[str]
    category: Optional[str] = Field(default='food | health | fashion | electronics | sports | vahicle | furniture | literature | other')
    price: Optional[int]
    quantity : Optional[int]

class Order(SQLModel):
    product_id: UUID
    quantity: int

class OrderPlace(Order, table=True):
    order_id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)    
    product_price: int
    product_name: str
    product_category: str
    totle_price: int
