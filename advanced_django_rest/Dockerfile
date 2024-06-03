FROM python:3.9

LABEL maintainer="rickrribeiro.github.io"

# Avoids buffering stdout and stderr
ENV PYTHONUNBUFFERED 1 

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./scripts /scripts
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    postgresql-client \
    jpeg-dev \
    zlib \
    zlib-dev \
    linux-headers \
    libpq-dev && \
    python -m venv /py && \
    /py/bin/pip install --no-cache-dir --upgrade pip && \
    /py/bin/pip install --no-cache-dir -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ]; then /py/bin/pip install --no-cache-dir -r /tmp/requirements.dev.txt; fi && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol && \
    chmode -R +x /scripts


ENV PATH="/scripts:/py/bin:$PATH"

USER django-user

CMD ["run.sh"]