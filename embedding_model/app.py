from flask import Flask, request, jsonify
from transformers import AutoModel, AutoTokenizer
import torch

app = Flask(__name__)

# Load the embedding model
tokenizer = AutoTokenizer.from_pretrained("e5-mistral-7b")
model = AutoModel.from_pretrained("e5-mistral-7b")

@app.route('/embed', methods=['POST'])
def embed():
    text = request.json['text']
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state
    return jsonify(embeddings.numpy().tolist())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
