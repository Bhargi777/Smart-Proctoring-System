.PHONY: init test run clean

init:
	python3 -m venv venv
	source venv/bin/activate && pip install --upgrade pip
	source venv/bin/activate && pip install -r requirements/base.txt -r requirements/dev.txt

test:
	source venv/bin/activate && pytest

run:
	source venv/bin/activate && python -m src.main

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf logs/
	rm -rf venv/
