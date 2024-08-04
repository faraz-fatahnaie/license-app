# license-app

### Configuration

1. **Create a `.env` file in the project root and add your database URL:**

    ```sh
    DATABASE_URL="postgresql://user:password@localhost/license_db"
    API_KEY="e8535b40a360e938330aaf7409e0b44def8778923c76318a7edd6ee3949b8b9b"
    REG_API_KEY="1a3e2ad26b6a60e9bfd50a0c814c495d5cf1d0431a177db54b257df9928a54b2"
    ```

### Database Migrations

1. **Initialize the Alembic directory (if not already initialized):**

    ```sh
    alembic init alembic
    ```

2. **Create a new migration:**

    ```sh
    alembic revision --autogenerate -m "Initial migration"
    ```

3. **Apply the migration:**

    ```sh
    alembic upgrade head
    ```

### Running the Application

1. **Start the FastAPI application:**

    ```sh
    uvicorn main:app --reload
    ```

    This will start the application on `http://127.0.0.1:8000`.
