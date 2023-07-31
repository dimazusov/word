.PHONY: run
build:
	docker build -t word .

run:
	docker run -dit -p 5000:5000 --name word word

stop:
	docker stop word