FROM python:3.11-alpine
RUN apk update && apk upgrade
RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev
RUN apk add --no-cache ffmpeg

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Cài đặt các dependency
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Thiết lập biến môi trường
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Mở cổng 8000
EXPOSE 8000

# Lệnh khởi động server
CMD ["gunicorn", "storyOnline.wsgi:application", "--bind", "0.0.0.0:8000"]