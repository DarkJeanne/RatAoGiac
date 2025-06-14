import os

# API Keys
COHERE_API_KEY = "LSsVgNhEJmAWepOBmRNcSwXABh18VtmMXWYGLpD2" # pls don't abuse this
GOOGLE_API_KEY = "AIzaSyBc7AuBLTYH1aGb0sk2MExIcEuT1vf1Cs0" #pls don't abuse it please
# Cấu hình model
embedding_model_name = "bkai-foundation-models/vietnamese-bi-encoder"
cohere_reranking_model_name = "rerank-multilingual-v3.0"
ollama_model_name = "llama3:8b-instruct-q4_0"
device = "cuda"

# Cấu hình chunking
PARENT_CHUNK_SIZE = 2000
PARENT_CHUNK_OVERLAP = 200
CHILD_CHUNK_SIZE = 300
CHILD_CHUNK_OVERLAP = 100

# Paths for storing data
DATA_DIR = "data"
VECTOR_STORES_DIR = os.path.join(DATA_DIR, "vector_stores")
CHAT_HISTORIES_DIR = os.path.join(DATA_DIR, "chat_histories")

# Ensure directories exist
os.makedirs(VECTOR_STORES_DIR, exist_ok=True)
os.makedirs(CHAT_HISTORIES_DIR, exist_ok=True) 