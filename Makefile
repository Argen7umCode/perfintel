CWD=$(shell pwd)


install_requirements:
	pip install -U -r requirements.txt

run: 
	python3 src/app.py