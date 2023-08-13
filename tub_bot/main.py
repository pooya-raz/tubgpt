from openai_service import get_response
print("Hello, I'm TubBot 🤖. How can I help?")
quit = False
while quit == False:
    query = input()
    if query == "quit":
        break
    response = get_response(query)
    print(response+"\n")