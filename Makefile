.PHONY: run build daemon

build:
	$ docker build -t marazmiki/flaskycapt .

dev:
	$ docker run \
		--rm \
		--name=flaskycapt \
		--publish=8765:8765 \
		-it marazmiki/flaskycapt:latest

daemon:
	$ docker run \
		--name=flaskycapt \
		--detach=true \
		--publish=8765:8765 \
		marazmiki/flaskycapt:latest
