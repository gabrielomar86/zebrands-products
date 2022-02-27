FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

COPY . .

RUN ls -la 

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
