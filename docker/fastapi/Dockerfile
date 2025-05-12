# مرحلة البناء
FROM python:3.11-slim as builder

WORKDIR /app
COPY app/requirements.txt .

RUN pip install --upgrade pip
RUN mkdir -p /install
RUN pip install --prefix=/install -r requirements.txt

# مرحلة التشغيل
FROM python:3.11-alpine

WORKDIR /app
COPY --from=builder /install /usr/local
COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
