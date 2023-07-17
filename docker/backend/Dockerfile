FROM python:alpine3.10

RUN apk add --update nodejs npm

COPY /src /app/src
COPY /requirements /app/requirements
COPY alembic.ini /app
COPY app.py /app
COPY .env.local /app
COPY package.json /app
COPY alembic.ini /app

WORKDIR /app

ENV ENVIRONMENT "local"

RUN pip install --upgrade pip

RUN pip install -r ./requirements/requirements.txt

RUN npm install

CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]


