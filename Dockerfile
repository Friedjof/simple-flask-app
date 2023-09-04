FROM python:3.11.0a1-alpine3.14

WORKDIR /app

COPY ./app.py app.py
COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]