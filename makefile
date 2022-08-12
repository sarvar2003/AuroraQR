run: 
	docker-compose up

stop:
	docker-compose stop

shell:
	docker-compose run --rm web python manage.py shell

superuser:
	docker-compose run --rm web python manage.py superuser

migrations:
	docker-compose run --rm web python maanage.py makemigrations