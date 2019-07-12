FROM python:3.7

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["uwsgi", "--http=0.0.0.0:8080", "--wsgi-file=run.py", "--callable=app"]
