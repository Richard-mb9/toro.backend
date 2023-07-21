FROM python:alpine3.10

COPY . /app

WORKDIR /app

ENV ENVIRONMENT "local"

RUN pip install --upgrade pip

RUN pip install -r ./requirements/requirements.txt

ENTRYPOINT ["sh", "./startup.sh"]


