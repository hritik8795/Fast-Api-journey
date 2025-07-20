from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load the correct .env file based on APP_ENV
env = os.getenv("APP_ENV", "development")

if env == "staging":
    load_dotenv(".env.staging")
elif env == "production":
    load_dotenv(".env.production")
else:
    load_dotenv(".env")  # default


class Settings(BaseSettings):
    APP_ENV: str = "development"
    DATABASE_URL: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
