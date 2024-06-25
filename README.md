# Mart API Project with Authentication and Authorization

## Project Overview

This project is an API for a mart system that supports product management, order placement, and user authentication and authorization. It utilizes FastAPI for the backend, PostgreSQL for the database, and Docker for containerization. The project is structured with multiple services including an API service, an authentication service, a PostgreSQL database, and an SMTP service for email notifications.

## Project Structure

The project consists of the following services:

1. **API Service**: Handles product and order-related operations.
2. **Auth Service**: Manages user authentication and authorization.
3. **PostgreSQL Database**: Stores user, product, and order data.
4. **SMTP Service**: Handles email notifications for user registration and account verification.

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Poetry (for managing Python dependencies)

### Installation and Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/iamshoaibxyz/mart-projects.git
    cd 7-basic-mart-with-auth
    ```

2. **Setup Environment Variables**:

    Create a `.env` file in the root directory and add the following environment variables:

    ```env
    DATABASE_URL=postgresql://shoaib:mypassword@db:5432/mydatabase
    JWT_SECRET=your_jwt_secret
    JWT_ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    USER_CONTEXT=your_user_context
    ```

3. **Build and Run the Services**:

    Use Docker Compose to build and start the services:

    ```bash
    docker-compose up --build
    ```

    This will start the following services:
    - API service on port 8000
    - Auth service on port 8002
    - PostgreSQL database on port 5432
    - SMTP service on ports 8025 (web interface) and 1025 (SMTP server)

### API Endpoints

#### API Service

- **GET /**: Root endpoint for the API service.
- **POST /order/**: Place an order.
- **GET /get-all-products**: Retrieve all products.
- **GET /get-products-by-category/{product_category}**: Retrieve products by category.
- **GET /get-product/{product_id}**: Retrieve a specific product by ID.
- **POST /add-product**: Add a new product.
- **PATCH /increment_product_item/{product_id}**: Increment product quantity.
- **PATCH /update_product/{product_id}**: Update product details.
- **GET /get_orders**: Retrieve all orders.

#### Auth Service

- **POST /auth/signup**: Create a new user account.
- **POST /auth/login**: User login.
- **POST /auth/account-verify**: Verify user account.
- **GET /auth/users**: Retrieve all user accounts (requires authentication).
- **GET /auth/tokens**: Retrieve all user tokens (requires authentication).

### Example Usage

1. **User Signup**:

    ```bash
    curl -X POST "http://127.0.0.1:8002/auth/signup" -H "Content-Type: application/json" -d '{"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "password": "StrongPassword123!"}'
    ```

2. **User Login**:

    ```bash
    curl -X POST "http://127.0.0.1:8002/auth/login" -H "Content-Type: application/x-www-form-urlencoded" -d "username=john.doe@example.com&password=StrongPassword123!"
    ```

3. **Add Product**:

    ```bash
    curl -X POST "http://127.0.0.1:8000/add-product" -H "Content-Type: application/json" -H "Authorization: Bearer <token>" -d '{"name": "Apple", "category": "food", "price": 1, "quantity": 100}'
    ```

4. **Place Order**:

    ```bash
    curl -X POST "http://127.0.0.1:8000/order/" -H "Content-Type: application/json" -H "Authorization: Bearer <token>" -d '{"product_id": "<product_uuid>", "quantity": 2}'
    ```

### Additional Notes

- Ensure the JWT secret is kept secure and not shared publicly.
- For email functionality, update the SMTP configuration in `app/config/email.py` to match your email server settings.

### Troubleshooting

- **Database Connection Issues**: Ensure that the PostgreSQL service is running and accessible.
- **Authentication Errors**: Verify that the JWT token is correctly passed in the `Authorization` header.

This README provides a comprehensive guide to setting up and running the Mart API project, allowing developers to quickly get started and understand the project's functionality.