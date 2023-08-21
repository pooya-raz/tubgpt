from openai_service import get_response, extract_context
import pinecone_service
from terminal_colors import colors

def colorText(text):
    return colors.OKCYAN + text + colors.ENDC

print(colorText("Hello, I'm TubBot 🤖. How can I help?"))
while True:
    query = input()
    if query == "quit":
        break
    # context = pinecone_service.query(query)
    #response = get_response(query, context)
    response = extract_context(query)
    print(response)
    #print(colorText(response) + "\n")