from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    PROJECT_NAME: str = "AI SOC Copilot"
    VERSION: str = "1.0.0"

    # PostgreSQL
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    # Redis
    REDIS_HOST: str

    # Qdrant
    QDRANT_URL: str

    # Neo4j
    NEO4J_URI: str
    NEO4J_USERNAME: str
    NEO4J_PASSWORD: str

    # OpenAI
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-4.1-mini"
    OPENAI_EMBEDDING_MODEL: str = "text-embedding-3-small"

    model_config = SettingsConfigDict(
        env_file=".env"
    )

    # ----------------------------
# Threat Intelligence APIs
# ----------------------------

# VirusTotal API Key
VIRUSTOTAL_API_KEY: str = ""

# AbuseIPDB API Key
ABUSEIPDB_API_KEY: str = ""

settings = Settings()