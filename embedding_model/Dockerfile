FROM python:3.9

WORKDIR /app

COPY . /app
COPY ../packages /packages
COPY ../models/sentence-transformers-paraphrase-multilingual-MiniLM-L12-v2 /models/embedding_model

RUN pip install --no-index --find-links /packages -r requirements.txt

EXPOSE 8000

CMD ["python", "app.py"]
