FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
Run pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python" , "app.py"]
