build:
	docker compose build

down:
	docker compose down

up: build makemigrations migrate
	docker compose up -d

migrate:
	docker compose run --rm api python manage.py migrate

makemigrations:
	docker compose run --rm api python manage.py makemigrations

loaddata:
	docker compose run --rm api python manage.py loaddata data.json

deps:
	docker compose run --rm api poetry install

deps_lock:
	docker compose run --rm api poetry lock

user:
	docker compose run --rm api python manage.py createsuperuser

static:
	docker compose run --rm api python manage.py collectstatic --noinput --clear --no-post-process

bash:
	docker compose run --rm api /bin/sh

test: build makemigrations migrate
	docker compose run --rm api python manage.py test

coverage: build makemigrations migrate
	docker compose run --rm api coverage run --source='api' --omit='api/tests/*' manage.py test
	docker compose run --rm api coverage report
	docker compose run --rm api coverage xml
