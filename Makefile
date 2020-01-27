
build:
	pipenv sync
	pipenv lock -r > requirements.txt
	docker build -t arhea/awsctl:latest .

clean:
	pipenv clean
	rm -rf ./awsctl_cli.egg-info
	rm -rf ./dist
	rm -rf ./build

release: clean
	pipenv install
	pipenv lock -r > requirements.txt
	pipenv run python setup.py bdist_wheel --universal
	pipenv run python -m twine upload dist/*

test:
	docker build -t arhea/awsctl-debian:latest -f ./docker/Dockerfile.debian .
	docker build -t arhea/awsctl-ubuntu1604:latest -f ./docker/Dockerfile.ubuntu1604 .
	docker build -t arhea/awsctl-ubuntu1804:latest -f ./docker/Dockerfile.ubuntu1804 .
