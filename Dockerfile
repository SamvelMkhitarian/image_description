FROM python:3.9-slim

RUN apt-get update && apt-get install -y libgl1 libglib2.0-0 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
