# 1. Använd en lättvikts-Python-image
FROM python:3.10-slim

# 2. Sätt arbetsmappen i containern
WORKDIR /app

# 3. Kopiera endast requirements.txt först för bättre caching
COPY requirements.txt .

# 4. Installera beroenden
RUN pip install --no-cache-dir -r requirements.txt

# 5. Kopiera resten av projektfilerna
COPY . .

# 6. Exponera Flask-porten
EXPOSE 5000

# 7. Starta Flask-applikationen
CMD ["python", "app.py"]