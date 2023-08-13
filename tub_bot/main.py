from sentence_transformers import SentenceTransformer
import pinecone
from Config import Config
from diacritic_utils import replace_diacritics

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = ["""1. Ghunyat al-nuzūʿ ilā ʿilmay al-uṣūl wa-l-furūʿ  
   غنية النزوع إلى علمي الأصول والفروع  
   Ḥamza b. ʿAlī  
   (d. 585/1189)

   **Editions**
    * *Ghunyat al-nuzūʿ ilā ʿilmay al-uṣūl wa-l-furūʿ*, ed. Ibrāhīm al-Bahādurī (Qum: Muʾassasat al-Imām al-Ṣādiq, 1417/1994)
    * *Ghunyat al-nuzūʿ ilā ʿilmay al-uṣūl wa-l-furūʿ* (Tehran: Majlis-i Shūrā-yi Islāmī, 1390/2011-12)

   **Commentaries**
    * *Muʿtaqad al-imāmiyya*, unknown (d. 999/1599)
    * *Fiqh-i istidlālī/Tarjuma-yi bakhsh-i Ghunyat al-nuzūʿ ilā ʿilmay al-uṣūl wa-l-furūʿ*, Mahdī Anjawinizhād 

"""]

embeddings = model.encode(sentences)

pinecone.init(api_key=Config.api_key, environment=Config.environment)

index = pinecone.Index("tub")

data = [];
for sentence, embedding in zip(sentences, embeddings):
    id_with_diacritics = sentence.splitlines()[0]
    id = replace_diacritics(id_with_diacritics)
    row = (id, embedding.tolist(),{'text': sentence})
    data.append(row)

print(data)
index.upsert(data)