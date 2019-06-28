# Flask Example app

## Install

```
virtualenv venv
source venv/bin/activate

pip install -r requirements.txt
```

### Migration

```
FLASK_APP=run.py flask db upgrade
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
uwsgi --http=0.0.0.0:8080 --wsgi-file=run.py  --callable=app
```
