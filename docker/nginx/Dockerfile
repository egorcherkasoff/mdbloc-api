FROM nginx:mainline-alpine3.18-slim

COPY ./docker/nginx/default.conf /etc/nginx/conf.d/default.conf

RUN sed -i 's/\r$//' /etc/nginx/conf.d/default.conf