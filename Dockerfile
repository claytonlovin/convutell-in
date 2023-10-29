# Use a imagem oficial do Python
FROM python:3.11.5

WORKDIR /app

COPY app /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
