from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    query_text = data['query']

    # Get embeddings from embedding model
    embedding_response = requests.post('http://embedding_model:5000/embed', json={"sentences": [query_text]})
    embeddings = embedding_response.json()

    # Query vector DB
    vector_response = requests.post('http://vector_db:6333/collections/test_collection/points/search', json={
        "vector": embeddings[0],
        "top": 5
    })
    results = vector_response.json()

    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
