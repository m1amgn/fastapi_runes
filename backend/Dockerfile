FROM python:3.11-slim-buster
RUN apt-get update -y && apt-get install -y \
python3-dev python-tk python3-tk tk-dev
RUN pip install --upgrade pip
COPY req.txt .
RUN pip install -r req.txt

COPY . .

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
