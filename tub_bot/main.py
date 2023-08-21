from openai_service import get_response, extract_context
import pinecone_service
from terminal_colors import colors
import json

def colorText(text):
    return colors.OKCYAN + text + colors.ENDC

print(colorText("Hello, I'm TubBot 🤖. How can I help?"))
while True:
    query = input()
    if query == "quit":
        break
    # context = pinecone_service.query(query)
    #response = get_response(query, context)
    search_keywords_json = json.loads(extract_context(query))

    print(search_keywords_json)
    #print(colorText(response) + "\n")