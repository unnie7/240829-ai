import requests
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct

# Initialize Qdrant client
client = QdrantClient(host="localhost", port=6333)

# Sample data for initialization
points = [
    PointStruct(id=1, vector=[0.1, 0.2, 0.3], payload={"text": "Hello world"}),
    PointStruct(id=2, vector=[0.4, 0.5, 0.6], payload={"text": "Hi there"})
]

# Create a collection
client.recreate_collection(
    collection_name="test_collection",
    vector_size=3,
    distance="Cosine"
)

# Upload points
client.upsert(
    collection_name="test_collection",
    points=points
)
