from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    DATABASE_URL : str = "postgresql+asyncpg://postgres:Password@localhost:5432/fastapi_ecom"

    class config:
        env_file = ".env"

settings = Setting()