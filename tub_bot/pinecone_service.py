import pinecone
from Config import Config
from sentence_transformers import SentenceTransformer
from diacritic_utils import replace_diacritics

pinecone.init(api_key=Config.pinecone_api_key, environment=Config.pinecone_environment)
index = pinecone.Index("tub")
model = SentenceTransformer('all-MiniLM-L6-v2')

def query(query):
    xq = model.encode([query]).tolist()

    return index.query(xq, top_k=5, include_metadata=True)

def upsert(texts):
    embeddings = model.encode(texts)

    pinecone.init(api_key=Config.pinecone_api_key, environment=Config.pinecone_environment)

    index = pinecone.Index("tub")

    data = [];
    for text, embedding in zip(texts, embeddings):
        id_with_diacritics = text.splitlines()[0]
        id = replace_diacritics(id_with_diacritics)
        row = (id, embedding.tolist(),{'text': text})
        data.append(row)

    print(data)
    index.upsert(data)