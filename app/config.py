import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    """Application settings."""

    # GEMINI API key
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")

    # GEMINI embeddings model to use
    GEMINI_EMBEDDINGS_MODEL: str = os.getenv("GEMINI_EMBEDDINGS_MODEL", "gemini-pro")

    # Vector database settings
    VECTOR_DB_HOST: str = os.getenv("VECTOR_DB_HOST", "localhost")
    VECTOR_DB_PORT: int = int(os.getenv("VECTOR_DB_PORT", 6333))
    QDRANT_DB_COLLECTION: str = os.getenv("QDRANT_DB_COLLECTION", "enterprise_rag")

    # Other settings can be added here as needed


settings = Settings()
