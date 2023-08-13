import openai
from Config import Config

openai.api_key = Config.openapi_key

response = openai.ChatCompletion.create(
   model = "gpt-3.5-turbo",
   messages = [
       {"role": "user", "content": "What is chatgpt?"}
   ] 
)
print(response["choices"][0]["message"]["content"])