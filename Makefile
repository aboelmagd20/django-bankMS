build:
	docker compose -f local.yml up --build -d --remove-orphans

up:
	docker compose -f local.yml up -d

down:
	docker compose -f local.yml down

down-v:
	docker compose -f local.yml down -v

banker-conifg:
	docker compose -f local.yml config

makemigrations:
	docker compose -f local.yml run --rm api python manage.py makemigrations

migrate:
	docker compose -f local.yml run --rm api python manage.py migrate

collectstatic:
	docker compose -f local.yml run --rm api python manage.py collectstatic --noinput

superuser:
	docker compose -f local.yml run --rm api python manage.py createsuperuser

flush:
	docker compose -f local.yml run --rm api python manage.py flush

network:
	docker network inspect banker_local_nw

banker-db:
	docker compose -f local.yml exec postgres psql --username=aemagd --dbname=banker

