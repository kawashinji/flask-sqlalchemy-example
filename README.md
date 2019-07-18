# Flask Example app

## Install

```
virtualenv venv
source venv/bin/activate

pip install -r requirements.txt
```

### Migration

```
FLASK_APP=web.run flask db upgrade
```

## Usage

### Start Docker

```
docker-compose build
docker-compose up
```

### Start WebServer

```
source venv/bin/activate
uwsgi --http=0.0.0.0:8080 --wsgi-file=web/run.py  --callable=app
```

### Start Worker

```
source venv/bin/activate
python -m worker.run
```

## Development

### Docker

```
docker build -t flask-fargate -f docker/web/Dockerfile .
docker build -t flask-worker-fargate -f docker/worker/Dockerfile .
```
