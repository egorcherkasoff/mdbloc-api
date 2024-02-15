build:
	docker-compose build && docker-compose up --remove-orphans

down:
	docker-compose down

up:
	docker-compose up