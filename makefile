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
<<<<<<< HEAD

freeze:
	docker-compose run --rm web pip freeze > requirements.txt
=======
	
migrate:
	docker-compose run --rm web python maanage.py migrate
>>>>>>> 9bd37dae22ec138c5a41a243580660ad49c61edf
