FROM python:3.9

WORKDIR /app

COPY . /app
COPY ../packages /packages
COPY ../models/kogpt2 /models/llm

RUN pip install --no-index --find-links /packages -r requirements.txt

EXPOSE 8003

CMD ["python", "app.py"]
