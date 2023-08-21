from openai_service import get_response, extract_context
import pinecone_service
from terminal_colors import colors
import json
from tub_mediawiki_bot import searchTitle, searchAuthor


def colorText(text):
    return colors.OKCYAN + text + colors.ENDC


print(colorText("Hello, I'm TubBot 🤖. How can I help?"))
while True:
    query = input()
    if query == "quit":
        break
    # context = pinecone_service.query(query)
    keywords: dict[str,str] = json.loads(extract_context(query))
    context: str = ""
    if "title" in keywords and keywords["title"] != None:
        context += searchTitle(keywords["title"])
    if "person" in keywords and keywords["person"] != None:
        context += searchAuthor(keywords["person"], 'incategory: "Author"')
    
    response = get_response(query, context)

    print(colorText(response) + "\n")
