# Simple flask app
_Author: [Friedjof Noweck](https://github.com/friedjof)_

This is a simple flask app to understand the basics of flask and how to dockerize it.

## How to run
* manuel
    * install deps `pip install -r requirements.txt`
    * run it `python3 -m flask run --host=0.0.0.0`
* docker
    * run it `docker compose up -d`
    * stop it `docker compose down`
    * rebuild it `docker compose up -d --build`

## Tipps
Show all running containers
```bash
docker ps
```
List all images
```bash
docker images
```
Delete unused images
```bash
docker image prune -a
```

## Links
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)