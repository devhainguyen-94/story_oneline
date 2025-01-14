FROM python:3.11-alpine
ENV PYTHONUNBUFFERED=1
RUN apk update && apk upgrade
RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev
RUN apk add --no-cache ffmpeg
WORKDIR /usr/src/app
# COPY ./requirements.txt /app/
# RUN pip install -r requirements.txt

# COPY . /app

ENTRYPOINT [ "gunicorn", "core.wsgi", "-b", "0.0.0.0:8000"]
# COPY poetry.lock pyproject.toml /usr/src/app/
# RUN pip3 install poetry
# RUN poetry config virtualenvs.create false
# RUN poetry install -n --no-ansi