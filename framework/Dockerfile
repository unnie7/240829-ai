FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-index --find-links ../packages -r requirements.txt

EXPOSE 8002

CMD ["python", "app.py"]
