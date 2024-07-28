# license-app

### Configuration

1. **Create a `.env` file in the project root and add your database URL:**

    ```sh
    DATABASE_URL="postgresql://user:password@localhost/license_db"
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
