from sqlmodel import SQLModel, Field, Relationship
from typing import Literal, Optional, List
from datetime import datetime, timezone


# we have defined two SQLModel classes: Order and OrderItem
# These classes represent database tables and their relationships.
# Order Model:
# Represents an order placed by a user.

class Order(SQLModel, table=True):
    order_id: Optional[int] = Field(default=None, primary_key=True) # An optional integer (primary key) representing the order ID.
    user_id: int = Field(foreign_key="user.user_id")   # An integer representing the user who placed the order (foreign key to the user table).
    order_address: str = Field(max_length=60) #   A string (maximum length 60) representing the delivery address.
    total_price: float                        # A float representing the total price of the order.
    advance_price: Optional[float]            # An optional float for advance payment (if applicable).
    order_type: Literal["Booking", "Ready made"] # A literal type (either “Booking” or “Ready made”) indicating the order type.
    order_status: str = Field(default="pending") # A string representing the order status (default is “pending”).
    order_date: datetime = Field(default=datetime.now(timezone.utc))   # A datetime field with the current UTC timestamp.
    items: List["OrderItem"] = Relationship(back_populates="order") # A list of related OrderItem objects (one-to-many relationship)


class OrderItem(SQLModel, table=True):
    order_item_id: Optional[int] = Field(default=None, primary_key=True) #An optional integer (primary key) representing the order item ID.
    order_id: int = Field(foreign_key="order.order_id")                   # An integer representing the parent order (foreign key to the order table).
    product_id: int = Field(foreign_key="product.product_id")             #An integer representing the product associated with this item (foreign key to the product table).
    product_item_id: int = Field(foreign_key="productitem.item_id")       # An integer representing the specific product item (foreign key to the productitem table).
    product_size_id: int = Field(foreign_key="productsize.product_size_id") # An integer representing the size of the product (foreign key to the productsize table).
    quantity: int = Field(gt=0)                                             #  An integer (greater than 0) indicating the quantity of this item.
    order: Optional[Order] = Relationship(back_populates="items") # A reference to the parent Order object (back-populates the relationship).
 