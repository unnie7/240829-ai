from qdrant_client import QdrantClient
from flask import Flask, request, jsonify

app = Flask(__name__)
client = QdrantClient(host='localhost', port=6333)

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    query_vector = data['vector']
    search_result = client.search(
        collection_name="bank_service",
        query_vector=query_vector,
        limit=3
    )
    return jsonify(search_result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)
