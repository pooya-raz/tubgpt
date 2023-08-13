from openai_service import get_response
import pinecone_service
from terminal_colors import colors

print(colors.OKCYAN + "Hello, I'm TubBot 🤖. How can I help?" + colors.ENDC)
while True:
    query = input()
    if query == "quit":
        break
    context = pinecone_service.query(query)
    response = get_response(query, context)
    print(response+"\n")