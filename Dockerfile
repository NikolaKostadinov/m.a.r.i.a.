FROM python:3.10

WORKDIR /app

RUN pip install json argparse subprocess

COPY . .

CMD [ "python", "./main.py" ]