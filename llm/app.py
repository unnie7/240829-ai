from transformers import AutoModelForCausalLM, AutoTokenizer
from flask import Flask, request, jsonify

app = Flask(__name__)

model = AutoModelForCausalLM.from_pretrained("distilgpt2")
tokenizer = AutoTokenizer.from_pretrained("distilgpt2")

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data['prompt']
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=50, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8003)
