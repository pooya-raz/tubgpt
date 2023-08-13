import openai
from Config import Config

openai.api_key = Config.openapi_key

def get_response(query, context):
    tripleQuote = '"""'
    content = tripleQuote+ context + tripleQuote + query
    response=  openai.ChatCompletion.create(
       model = "gpt-3.5-turbo",
       messages = [
             {"role": "system", "content": "Answer questions with the data given in triple quotes"},
           {"role": "user", "content": content}
       ] 
    )
    return response["choices"][0]["message"]["content"]