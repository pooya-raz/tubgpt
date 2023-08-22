import openai
import config

openai.api_key = config.openapi_key

tripleQuote = '"""'


def extract_context(query:str) -> str:
    content = tripleQuote + query + tripleQuote
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Exctract the title and or person from the question in triple quotes. Unknown values are null. Return as json",
            },
            {"role": "user", "content": content},
        ],
    )
    return response["choices"][0]["message"]["content"]


def get_response(query: str, context: str) -> str:
    content = tripleQuote + context + tripleQuote + query
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "As a bibliographic database of Twevlver usul al-fiqh, answer questions with the data given in triple quotes",
            },
            {"role": "user", "content": content},
        ],
    )
    return response["choices"][0]["message"]["content"]
