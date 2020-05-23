.PHONY: test install pep8 clean

test: 
	py.test --cov-config .coveragerc --cov=revolut

unit_test: 
	py.test revolut/tests/unit/

integration_test: 
	py.test revolut/tests/integration/

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
	python revolut/utils/docker.py && \
	sleep 5s && \
	flask run

rest_stop:
	docker-compose -f /tmp/docker-compose.yml down -v

cli_run:
	cat example_input.json | python revolut/cli/nest.py currency country city

rest_post:
	curl -u revolut:challenge2019 -vX POST 'http://localhost:5000/parse?nest=currency&nest=country&nest=city' -d @example_input.json \
--header "Content-Type: application/json"

start_db:
	python revolut/utils/docker.py && \
	sleep 5s && \
	python initial_postgres_setup.py && \
	flask db upgrade && \
	flask adduser -u revolut -p challenge2019

stop_db:
	docker stop revolut
	docker rm revolut