from qdrant_client import QdrantClient
from qdrant_client.http import models
import numpy as np

# Connect to the Qdrant service
client = QdrantClient(host="localhost", port=6333)

# Initialize the collection with vector embeddings
client.recreate_collection(
    collection_name="my_vectors",
    vectors_config=models.VectorParams(
        size=768,  # The dimension of your vectors
        distance=models.Distance.COSINE
    )
)

# Sample data to populate the database
sample_vectors = np.random.rand(10, 768).tolist()  # Random sample vectors
sample_payload = [{"doc_id": f"doc_{i}", "content": f"Sample document {i}"} for i in range(10)]

# Upload sample vectors
client.upload_collection(
    collection_name="my_vectors",
    vectors=sample_vectors,
    payload=sample_payload,
    ids=None
)
