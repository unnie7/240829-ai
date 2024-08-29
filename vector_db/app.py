from flask import Flask, request, jsonify
from qdrant_client import QdrantClient
import numpy as np

app = Flask(__name__)

# Connect to the Qdrant service
client = QdrantClient(host="localhost", port=6333)

@app.route('/store_vector', methods=['POST'])
def store_vector():
    data = request.json
    vector = data['vector']
    payload = data.get('payload', {})
    
    response = client.upsert(
        collection_name="my_vectors",
        points=[models.PointStruct(id=payload.get('doc_id', None), vector=vector, payload=payload)]
    )
    
    return jsonify({"status": "success", "response": response})

@app.route('/search', methods=['POST'])
def search():
    query_vector = request.json['vector']
    results = client.search(
        collection_name="my_vectors",
        query_vector=query_vector,
        limit=5  # Return top 5 results
    )
    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

