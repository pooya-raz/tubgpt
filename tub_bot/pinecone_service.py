import pinecone
from Config import Config
from sentence_transformers import SentenceTransformer

pinecone.init(api_key=Config.api_key, environment=Config.environment)
index = pinecone.Index("tub")
model = SentenceTransformer('all-MiniLM-L6-v2')

def query(query):
    xq = model.encode([query]).tolist()

    return index.query(xq, top_k=5, include_metadata=True)