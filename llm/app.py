from flask import Flask, request, jsonify
from vllm import VLLM, LLamaModel

app = Flask(__name__)

# Load vLLM model
vllm_model = VLLM(model=LLamaModel("meta-llama-3.1-8B"))

@app.route('/infer', methods=['POST'])
def infer():
    prompt = request.json['prompt']
    response = vllm_model(prompt)
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
