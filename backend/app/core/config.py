from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My Application"
    admin_email: str = "admin@example.com"
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()