FROM python:3.9-alpine

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /code

EXPOSE 8080

CMD ["python", "server.py"] 
