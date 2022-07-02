FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install -r ./requirements.txt

CMD [ "python", "main.py" ]