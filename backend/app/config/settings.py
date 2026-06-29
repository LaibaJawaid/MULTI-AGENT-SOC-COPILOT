from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "AI SOC Copilot"
    VERSION: str = "1.0.0"

    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    REDIS_HOST: str

    QDRANT_URL: str

    NEO4J_URI: str
    NEO4J_USERNAME: str
    NEO4J_PASSWORD: str

    OPENAI_API_KEY: str = ""

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()