# -------- STAGE 1: Base image to install dependencies --------
    FROM python:3.11-alpine AS builder

    WORKDIR /app
    
    # تثبيت أدوات النظام المطلوبة (مثلاً gcc و build tools)
    RUN apk add --no-cache gcc musl-dev libffi-dev
    
    # نسخ ملفات المتطلبات
    COPY ./requirements.txt .
    
    # تثبيت الحزم في مجلد مؤقت
    RUN pip install --upgrade pip \
        && pip install --prefix=/install -r requirements.txt
    
    # -------- STAGE 2: Final runtime image --------
    FROM python:3.11-alpine
    
    WORKDIR /app
    
    # نسخ الحزم من الستيج الأول
    COPY --from=builder /install /usr/local
    
    # نسخ كود التطبيق
    COPY . .
    
    # تعيين البورت
    EXPOSE 8000
    
    # الأمر الرئيسي لتشغيل FastAPI
    CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
    