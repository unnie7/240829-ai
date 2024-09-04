from sentence_transformers import SentenceTransformer
from flask import Flask, request, jsonify

app = Flask(__name__)
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

@app.route('/embed', methods=['POST'])
def embed_text():
    data = request.json
    text = data['text']
    embedding = model.encode(text).tolist()
    return jsonify({'embedding': embedding})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
