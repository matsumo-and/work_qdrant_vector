from typing import List
import numpy as np
import pandas as pd
from fastembed.embedding import TextEmbedding
from qdrant_client import QdrantClient


if __name__ == "__main__":

    # Example list of documents
    documents: List[str] = [
        "ハローワールド",
        "これはサンプルのドキュメントです。",
        "fastembed は Qdrant がサポート・保守を行っています。",
    ]

    # embedding_model = Embedding(model_name="intfloat/multilingual-e5-large", max_length=512)
    embedding_model = TextEmbedding()
    embeddings: List[np.ndarray] = list(embedding_model.embed(documents))

    for i in embeddings:
        print(i.shape)
        print(i[:5])




    # Initialize the client
    client = QdrantClient("qdrant", port=6333)

    # set model
    # client.set_model("intfloat/multilingual-e5-large")
    print(f"vector params = {client.get_fastembed_vector_params()}")

    client.recreate_collection(
        collection_name="artists_collection",
        vectors_config=client.get_fastembed_vector_params()
    )

    # import csv
    df = pd.read_csv('./output.csv')

    # ids
    ids = df[df.columns[0]].tolist()

    # metadata
    metadata = df.drop('detail', axis=1).to_dict(orient='records')

    # document
    documents = df[df.columns[2]].tolist()

    client.add(
        collection_name="artists_collection",
        documents=documents,
        metadata=metadata,
        ids=ids,
        parallel=0
    )

    print("----------------------------------")
    print("---------- set up done! ----------")
    print("----------------------------------")

    search_result = client.query(
        collection_name="artists_collection",
        query_text="best drummer."
    )
    print(search_result)