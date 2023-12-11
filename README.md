# Crawl

Crawl website crawler built with Celery, Redis, FastAPI, and Docker. It provides an API endpoint that crawls data of each corporate in the [Glass Dollar Ranking](https://ranking.glassdollar.com/) page, processes it in parallel using Celery, and returns the data in JSON format.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker is installed and running on your machine.
- Port 80 is available on your local machine.

## Installation

- Clone the repository to your local machine.
- Navigate to the project directory.
- Run the following command in the terminal:
 
  `docker-compose up`

## Usage

To use, send an HTTP GET request with your desired method to the following endpoint: http://localhost/crawl

## Swagger UI

Crawl also provides a Swagger UI for easier interaction. You can access it at the following URL:

http://localhost/api/v1/crawler/docs
