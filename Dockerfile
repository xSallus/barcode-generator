FROM python:alpine
WORKDIR /app

COPY requirements.txt .
COPY run.py .
COPY src ./src

VOLUME ${pwd}/db/

RUN mkdir ./src/templates/static/tmp/
RUN pip install -r requirements.txt --break-system-packages
