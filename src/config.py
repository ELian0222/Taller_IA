import os
from pathlib import Path

class AppConfig:
    # Rutas base del proyecto
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_DIR = BASE_DIR / "data"
    DOCS_DIR = BASE_DIR / "docs"
    
    # Configuración del modelo y embeddings con Ollama
    OLLAMA_MODEL = "llama3" # O el modelo que estés usando localmente
    EMBEDDING_MODEL = "nomic-embed-text" # O el que prefieras para embeddings
    
    # Configuración de Qdrant o almacenamiento local si aplica
    VECTOR_DB_DIR = BASE_DIR / "vector_db"