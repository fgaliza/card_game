deploy:
	git push heroku master

migrate:
	heroku run --app card-game "cd card_game && ./manage.py migrate"

shell:
	heroku run --app card-game "cd card_game && ./manage.py shell"

enable-local:
	@cp local.env .env

logs:
	heroku logs --tail --app card-game

info:
	heroku info --app card-game

lint:
	pipenv run pre-commit run -a -v

test:
	pipenv run pytest -x -s card_game

fixtures:
	python card_game/manage.py loaddata card_game/fixtures/*

runserver:
	python card_game/manage.py runserver