FROM python:alpine3.10

RUN apk add --update nodejs npm

COPY /src /app/src
COPY /alembic /app/alembic
COPY app.py /app
COPY .env.local /app
COPY requirements.txt /app
COPY package.json /app
COPY alembic.ini /app
COPY update_database.sh /app
COPY startup.sh /app

WORKDIR /app

ENV ENVIRONMENT "local"

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN npm install

CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]


