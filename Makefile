.PHONY: up down build restart logs api-logs etl sentiment test

up:
	docker compose up

down:
	docker compose down

build:
	docker compose up --build

restart:
	docker compose restart

logs:
	docker compose logs -f

api-logs:
	docker compose logs -f api

etl:
	docker compose exec api python -m src.etl.pipeline data/raw/reviews.csv

sentiment:
	docker compose exec api python -m src.ml.sentiment.updater

test:
	.venv/Scripts/python.exe -m pytest tests/ -v
