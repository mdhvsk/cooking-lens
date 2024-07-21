import os

from astrapy.db import AstraDB

# Initialize the client. The namespace parameter is optional if you use
# "default_keyspace".
db = AstraDB(
    token=os.environ["ASTRA_DB_APPLICATION_TOKEN"],
    api_endpoint=os.environ["ASTRA_DB_API_ENDPOINT"],
    namespace="default_keyspace",
)
print(db)

# Create a collection
collection = db.create_collection("vector_test", dimension=5, metric="cosine")
print(collection)

# ⬆️ NEW CODE

documents = [
    {
        "_id": "1",
        "text": "ChatGPT integrated sneakers that talk to you",
        "$vector": [0.1, 0.15, 0.3, 0.12, 0.05],
    },
    {
        "_id": "2",
        "text": "An AI quilt to help you sleep forever",
        "$vector": [0.45, 0.09, 0.01, 0.2, 0.11],
    },
    {
        "_id": "3",
        "text": "A deep learning display that controls your mood",
        "$vector": [0.1, 0.05, 0.08, 0.3, 0.6],
    },
]
res = collection.insert_many()
print(res)

# Delete the collection
# res = db.delete_collection(collection_name="vector_test")
# print(res)

