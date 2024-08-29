from flask import Flask, request, render_template, jsonify
import requests

app = Flask(__name__)

# Root route to display the web interface
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']

        # Step 1: Get the vector for the input query
        embed_response = requests.post('http://embedding_model:5002/embed', json={'text': query})
        embedding = embed_response.json()['embedding']

        # Step 2: Search for similar vectors in the vector database
        search_response = requests.post('http://vector_db:5001/search', json={'vector': embedding})
        search_results = search_response.json()['results']

        # Step 3: Extract the most relevant document's content
        if search_results:
            top_document = search_results[0]['payload']['content']
        else:
            top_document = "No relevant documents found."

        # Step 4: Generate the final response using the LLM
        infer_response = requests.post('http://llm:5003/infer', json={'prompt': f"{query} {top_document}"})
        final_answer = infer_response.json()['answer']

        # Render the results in the web interface
        return render_template('index.html', query=query, embedding=embedding, search_results=search_results, top_document=top_document, final_answer=final_answer)

    return render_template('index.html')


# API route to retrieve the final answer directly (for AJAX or API access)
@app.route('/api/infer', methods=['POST'])
def infer():
    data = request.json
    query = data['query']

    # Step 1: Get the vector for the input query
    embed_response = requests.post('http://embedding_model:5002/embed', json={'text': query})
    embedding = embed_response.json()['embedding']

    # Step 2: Search for similar vectors in the vector database
    search_response = requests.post('http://vector_db:5001/search', json={'vector': embedding})
    search_results = search_response.json()['results']

    # Step 3: Extract the most relevant document's content
    if search_results:
        top_document = search_results[0]['payload']['content']
    else:
        top_document = "No relevant documents found."

    # Step 4: Generate the final response using the LLM
    infer_response = requests.post('http://llm:5003/infer', json={'prompt': f"{query} {top_document}"})
    final_answer = infer_response.json()['answer']

    return jsonify({
        'query': query,
        'embedding': embedding,
        'search_results': search_results,
        'top_document': top_document,
        'final_answer': final_answer
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
