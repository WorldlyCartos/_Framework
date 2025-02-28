# config.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_username: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str
    db_odbc_driver: str

    class Config:
        env_file = ".env"  # This tells Pydantic to load the .env file


settings = Settings()
