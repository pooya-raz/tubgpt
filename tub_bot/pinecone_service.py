import pinecone
import config
from sentence_transformers import SentenceTransformer
from diacritic_utils import replace_diacritics
import os

os.environ["TOKENIZERS_PARALLELISM"] = "false" #Disable parallelism in transformers otherwise it will throw a warning
pinecone.init(api_key=config.pinecone_api_key, environment=config.pinecone_environment)
index = pinecone.Index("tub")
model = SentenceTransformer('all-MiniLM-L6-v2')

def query(query):
    xq = model.encode([query]).tolist()
    result = index.query(xq, top_k=3, include_metadata=True)
    response = ""
    for match in result["matches"]:
        response += match["metadata"]["text"] + "\n"
    return response

def upsert(texts):
    embeddings = model.encode(texts)

    pinecone.init(api_key=config.pinecone_api_key, environment=config.pinecone_environment)

    index = pinecone.Index("tub")

    data = [];
    for text, embedding in zip(texts, embeddings):
        id_with_diacritics = text.splitlines()[0]
        id = replace_diacritics(id_with_diacritics)
        row = (id, embedding.tolist(),{'text': text})
        data.append(row)

    print(data)
    index.upsert(data)

# Sample code on how to update the database
# upsert([data.text1, data.text2, data.text3])