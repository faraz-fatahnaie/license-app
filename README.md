# license-app

export DATABASE_URL="postgresql://user:password@localhost/license_db"

$ alembic init alembic

$ alembic revision --autogenerate -m "Initial migration"
$ alembic upgrade head

$ uvicorn main:app --reload
