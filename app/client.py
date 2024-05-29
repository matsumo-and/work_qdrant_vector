from dotenv import load_dotenv
load_dotenv()

import os
import qdrant_client

OPEN_AI_API_KEY = os.getenv('OPENAIAPIKEY')

embeddings = OpenAIEmbeddings()

client = qdrant_client.QdrantClient(
    host="localhost",
    prefer_grpc=True,
)

response = client.get_collections()
print(response)