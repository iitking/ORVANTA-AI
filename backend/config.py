import os
from typing import List, Optional

try:
    from pydantic_settings import BaseSettings
    from pydantic import Field

    class Settings(BaseSettings):
        PROJECT_NAME: str = "ORVANTA AI"
        VERSION: str = "0.1.0"
        API_V1_PREFIX: str = "/api/v1"
        ENVIRONMENT: str = Field(default="development", env="ENVIRONMENT")
        DEBUG: bool = True
        SECRET_KEY: str = Field(default="dev-secret-key-orvanta-ai-super-secure-jwt-token-2026", env="SECRET_KEY")
        ALGORITHM: str = "HS256"
        ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

        DATABASE_URL: str = Field(
            default="sqlite+aiosqlite:///./orvanta.db",
            env="DATABASE_URL"
        )
        REDIS_URL: str = Field(default="redis://localhost:6379/0", env="REDIS_URL")

        QDRANT_HOST: str = Field(default="localhost", env="QDRANT_HOST")
        QDRANT_PORT: int = Field(default=6333, env="QDRANT_PORT")
        QDRANT_API_KEY: Optional[str] = Field(default=None, env="QDRANT_API_KEY")
        QDRANT_COLLECTION: str = Field(default="orvanta_knowledge_base", env="QDRANT_COLLECTION_NAME")

        OPENAI_API_KEY: Optional[str] = Field(default=None, env="OPENAI_API_KEY")
        ANTHROPIC_API_KEY: Optional[str] = Field(default=None, env="ANTHROPIC_API_KEY")
        GEMINI_API_KEY: Optional[str] = Field(default=None, env="GEMINI_API_KEY")
        DEFAULT_LLM_MODEL: str = Field(default="gpt-4o-mini", env="DEFAULT_LLM_MODEL")

        LANGCHAIN_TRACING_V2: bool = Field(default=False, env="LANGCHAIN_TRACING_V2")
        LANGCHAIN_API_KEY: Optional[str] = Field(default=None, env="LANGCHAIN_API_KEY")
        LANGCHAIN_PROJECT: str = Field(default="orvanta-ai", env="LANGCHAIN_PROJECT")

        N8N_BASE_URL: str = Field(default="http://localhost:5678", env="N8N_BASE_URL")
        N8N_API_KEY: Optional[str] = Field(default=None, env="N8N_API_KEY")

        CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000", "*"]

        class Config:
            env_file = ".env"
            extra = "allow"

    settings = Settings()

except ImportError:
    # Graceful fallback when running in minimal environments without pydantic_settings
    class FallbackSettings:
        PROJECT_NAME: str = "ORVANTA AI"
        VERSION: str = "0.1.0"
        API_V1_PREFIX: str = "/api/v1"
        ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
        DEBUG: bool = True
        SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-key-orvanta-ai-super-secure-jwt-token-2026")
        ALGORITHM: str = "HS256"
        ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24

        DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./orvanta.db")
        REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")

        QDRANT_HOST: str = os.getenv("QDRANT_HOST", "localhost")
        QDRANT_PORT: int = int(os.getenv("QDRANT_PORT", "6333"))
        QDRANT_API_KEY: Optional[str] = os.getenv("QDRANT_API_KEY", None)
        QDRANT_COLLECTION: str = os.getenv("QDRANT_COLLECTION_NAME", "orvanta_knowledge_base")

        OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY", None)
        ANTHROPIC_API_KEY: Optional[str] = os.getenv("ANTHROPIC_API_KEY", None)
        GEMINI_API_KEY: Optional[str] = os.getenv("GEMINI_API_KEY", None)
        DEFAULT_LLM_MODEL: str = os.getenv("DEFAULT_LLM_MODEL", "gpt-4o-mini")

        LANGCHAIN_TRACING_V2: bool = os.getenv("LANGCHAIN_TRACING_V2", "false").lower() == "true"
        LANGCHAIN_API_KEY: Optional[str] = os.getenv("LANGCHAIN_API_KEY", None)
        LANGCHAIN_PROJECT: str = os.getenv("LANGCHAIN_PROJECT", "orvanta-ai")

        N8N_BASE_URL: str = os.getenv("N8N_BASE_URL", "http://localhost:5678")
        N8N_API_KEY: Optional[str] = os.getenv("N8N_API_KEY", None)

        CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://127.0.0.1:3000", "*"]

    settings = FallbackSettings()
