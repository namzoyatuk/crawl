# Crawl
Website crawler using Celery, Redis, FastAPI and Docker

Provides an API endpoint that crawls data of each corporate in the https://ranking.glassdollar.com/ via Celery processes in parallel and returns the data in JSON format.


## Prerequisites

- Docker is up and running
- In your local machine port 80 must be available

## Run

- In the project directory run in terminal `docker-compose up`
- Send an HTTP GET request with your desired method to http://localhost/crawl

## Swagger UI

You can also use Swagger UI in order to make a request.
http://localhost/api/v1/crawler/docs
