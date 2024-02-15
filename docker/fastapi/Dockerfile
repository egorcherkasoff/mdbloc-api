FROM python:3.11.3-slim-bullseye

WORKDIR /app

COPY ./requirements.txt .


RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

COPY ./docker/fastapi/start.sh /start

RUN sed -i 's/\r$//' /start

RUN chmod +x /start

