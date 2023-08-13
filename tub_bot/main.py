from openai_service import get_response
from terminal_colors import colors

print(colors.OKCYAN + "Hello, I'm TubBot 🤖. How can I help?" + colors.ENDC)
while True:
    query = input()
    if query == "quit":
        break
    response = get_response(query)
    print(response+"\n")