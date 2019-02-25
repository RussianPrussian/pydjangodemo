FROM python:3.6.8-alpine3.9
WORKDIR /demosolst
COPY . /demosolst
RUN apk add --no-cache postgresql-libs && \
    apk --update add postgresql-client && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install gunicorn && \
    pip install -r requirements.txt && \
    chmod 500 startup.sh
EXPOSE 8000
CMD ["./startup.sh"]