# TubGPT

Integrates TUB data with ChatGPT.

It uses sbert to create vectors for chunks of the TUB data, then uploads them to pinecone. Then it uses ChatGPT to generate responses to user input, and uses pinecone to find the closest TUB data chunk to the generated response.

## Running the application
1. Requires a config.py file in the tub_bot folder that contains API keys for pincone and openai.
2. Install dependecies with poetry `poetry install`
3. Will need to upload some test data to pinecone. See the comment in `pinecone_service.py`. Then run `poetry run python tub_bot/pinecone_service.py`
4. Run the application with `poetry run python tub_bot/main.py`

## Running the tests
There are no tests

## Dependencies
- [Pinecone](https://www.pinecone.io/)
- [OpenAI](https://openai.com/)
- [SBERT](https://www.sbert.net/)