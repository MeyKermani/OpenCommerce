FROM python:3.12-slim
WORKDIR /app
COPY requierments.txt .
RUN pip install --no-cache-dir -r requierments.txt
COPY . .
CMD ["python", "manage.py","runserver","0.0.0.0:8000"]
