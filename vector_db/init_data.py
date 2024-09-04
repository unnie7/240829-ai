from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance
from embedding_model.app import embed_text

def create_qdrant_collection():
    client = QdrantClient(host='localhost', port=6333)
    client.recreate_collection(
        collection_name="bank_service",
        vector_size=384,
        distance=Distance.COSINE
    )
    return client

def insert_sample_data(client):
    data = [
        {"conversation_id": "1", "sender": "customer", "message": "안녕하세요, 순번을 받고 싶어요.", "timestamp": "2024-08-10T10:00:00Z"},
        {"conversation_id": "1", "sender": "ai_banker", "message": "안녕하세요! 어떤 업무를 보시려고 하나요?", "timestamp": "2024-08-10T10:00:05Z"}
    ]
    
    points = [
        {
            'id': i, 
            'vector': embed_text(data[i]['message']), 
            'payload': data[i]
        } for i in range(len(data))
    ]
    
    client.upsert(
        collection_name="bank_service",
        points=points
    )

if __name__ == "__main__":
    client = create_qdrant_collection()
    insert_sample_data(client)
    print("Sample data inserted successfully!")
