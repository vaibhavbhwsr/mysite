FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /webapp

COPY . /webapp/

RUN pip install --upgrade pip
RUN pip install -r requirements.dev.txt

RUN sed -i 's/\r$//g' /webapp/entrypoint.sh
RUN chmod +x /webapp/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/webapp/entrypoint.sh"]