FROM python:3.13-slim

WORKDIR /app

# Copier requirements.txt (à créer avec pytest, selenium, flask, flask_sqlalchemy)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
