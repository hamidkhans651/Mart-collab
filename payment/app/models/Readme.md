learn about sqlmodels

1. **Scenario**:
   - Imagine you're building an e-commerce platform.
   - You need to store information about products, such as their names, prices, and descriptions.

2. **SQLModel Model Example**:
   - Suppose you want to represent a **product** in your database.
   - You create a Python class called `Product` using SQLModel.
   - Each attribute of the class corresponds to a column in the database table.

3. **Python Code**:
   ```python
   from sqlmodel import SQLModel, Field

   class Product(SQLModel, table=True):
       product_id: int = Field(default=None, primary_key=True)
       name: str
       price: float
       description: str
   ```

4. **Explanation**:
   - The `Product` class is a SQLModel model.
   - It has three attributes:
     - `product_id`: An integer (primary key) representing the unique ID of the product.
     - `name`: A string representing the product's name.
     - `price`: A float representing the product's price.
     - `description`: A string describing the product.

5. **Usage**:
   - You can create instances of the `Product` class to represent individual products.
   - For example:
     ```python
     product1 = Product(name="Smartphone", price=599.99, description="High-end mobile device")
     product2 = Product(name="Laptop", price=1299.99, description="Powerful laptop for professionals")
     ```

6. **Database Interaction**:
   - When you save these instances to the database, they become rows in the `Product` table.
   - You can query, update, or delete products using Python code, without writing raw SQL statements.

## WHY WE USE CLASSES IN MODEL 

Models (Classes):
Purpose: Models represent the structure of your data. They define the schema for your database tables or API responses.
Why Classes?:
Classes allow you to define attributes (fields) and methods (functions) together.
Models often have fields (attributes) that map directly to database columns.
Using classes provides a clear and organized way to represent data.

