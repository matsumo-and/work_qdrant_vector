from ast import literal_eval
from dotenv import load_dotenv
load_dotenv()

import os
import qdrant_client
import pandas as pd
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from qdrant_client.http import models as rest
import openai

import json

OPEN_AI_API_KEY = os.getenv('OPENAIAPIKEY')

#embeddings = OpenAIEmbeddings()

df = pd.read_csv('./output.csv')
df["embeddings"] = df.embeddings.apply(literal_eval)

client = qdrant_client.QdrantClient(
    host="qdrant",
    prefer_grpc=True,
)

response = client.get_collections()
print(response)

client = QdrantClient(":memory:")

vector_size = len(df["embeddings"][0])

client.recreate_collection(
    collection_name="HistoricalFigures",
    vectors_config={
        "content": rest.VectorParams(
            distance=rest.Distance.COSINE,
            size=vector_size,
        ),
    }
)

client.upsert(
    collection_name="HistoricalFigures",
    points=[
        rest.PointStruct(
            id=k,
            vector={
                "content": v["embeddings"],
            },
            payload=v.to_dict(),
        )
        for k, v in df.iterrows()
    ],
)
# 全てのポイントが保存されていることを確認するためにコレクションのサイズを確認
client.count(collection_name="HistoricalFigures")

results = query_qdrant("最も偉大なシンガーは？", "HistoricalFigures")
for i, content in enumerate(results):
    json_obj = json.loads(content.payload["properties"])
    name = json_obj["person_name"]
    print(f"{i + 1}. {name} (Score: {round(content.score, 3)})")


def query_qdrant(query, collection_name, vector_name="content", top_k=10):
    embedded_query = openai.Embedding.create(
        input=query,
        model="text-embedding-ada-002",
    )["data"][0]["embedding"]
    
    results = client.search(
        collection_name=collection_name,
        query_vector=(
            vector_name, embedded_query
        ),
        limit=top_k,
    )

    return results