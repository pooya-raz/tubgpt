# TubGPT

Integrates TUB data with ChatGPT.

The flow is as follows:

1. Generate embeddings of chunks of TUB data using SBERT.
2. Upload embeddings to Pinecone for storage and retrieval.
3. Leverage Pinecone to match of user queries with embeddings.
4. Employ the resultant matches as prompts for ChatGPT's dynamic interactions.
   
## Running the application
1. Requires a config.py file in the tub_bot folder that contains API keys for Pinecone and OpenAI.
2. Install dependecies with poetry `poetry install`
3. Will need to upload some test data to Pinecone. See the comment in `pinecone_service.py`. Then run `poetry run python tub_bot/pinecone_service.py`
4. Run the application with `poetry run python tub_bot/main.py`

## Running the tests
There are no tests

## Dependencies
- [Pinecone](https://www.pinecone.io/)
- [OpenAI](https://openai.com/)
- [SBERT](https://www.sbert.net/)
