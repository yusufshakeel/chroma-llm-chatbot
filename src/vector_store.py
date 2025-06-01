import chromadb
from chromadb.utils import embedding_functions
from env_config import CHROMA_DATABASE_PATH, COLLECTION_NAME

emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path=CHROMA_DATABASE_PATH)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=emb_fn
)
