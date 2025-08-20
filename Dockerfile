FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app.py app.py

# Add current directory to PYTHONPATH so app.py can be imported in tests
ENV PYTHONPATH=/app

CMD ["pytest"]
