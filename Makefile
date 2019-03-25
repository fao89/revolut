.PHONY: test install pep8 clean

test: 
	py.test  -v -p no:warnings --cov-config .coveragerc --cov=revolut -l --tb=short --maxfail=1 revolut/tests/

install:
	pip install --upgrade pip
	pip install -e "." --upgrade --no-cache

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	pip install -e .[dev] --upgrade --no-cache

rest_run:
	flask run

cli_run:
	cat example_input.json | python revolut/cli/nest.py currency country city

rest_post:
	curl -u revolut:challenge2019 -vX POST http://localhost:5000/parse?nest_currency__country__city -d @example_input.json \
--header "Content-Type: application/json"

start_db:
	flask db upgrade && flask adduser -u revolut -p challenge2019