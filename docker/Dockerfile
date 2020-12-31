FROM python:3.8-alpine

RUN apk add --no-cache \
        g++ \
        git \
        libffi-dev \
        libxslt-dev \
        mariadb-dev \
        jpeg-dev \
        zlib-dev \
        build-base

RUN python -m pip install --upgrade pip

COPY . /app/.
WORKDIR /app

RUN cd /app & \
    pip --no-cache-dir install -r requirements.txt

RUN rm -f .env \
 && rm -rf collected_static \
 && rm -rf media \
 && django-admin collectstatic --noinput --settings=mmdb.settings

CMD gunicorn mmdb.wsgi -c mmdb/gunicorn.py

EXPOSE ${MMDB_PORT}
