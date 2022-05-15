format:
	pipenv run black .

make lint:
	pipenv run pylint src

run:
	pipenv run python main.py

test:
	pipenv run pytest tests --cov=src

behave:
	pipenv run behave tests/features