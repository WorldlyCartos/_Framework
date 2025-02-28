from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..core.config import settings


DATABASE_URL = f"mssql+pyodbc://{settings.db_username}:{settings.db_password}@{settings.db_host}/{settings.db_name}?driver={settings.db_odbc_driver}"

engine = create_engine(url=DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency injection. Ensures single db instance per request.
def get_db():
    db = SessionLocal()
    try:
        yield db  # yield acts as a context manager. Calls to get_db will continue to the finally when transaction completes or fails.
    finally:
        db.close()
