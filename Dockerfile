FROM python:3.10.4

WORKDIR /app

COPY . .

CMD [ "python", "./main.py" ]