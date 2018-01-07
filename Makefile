help:
	@echo "    deps"
	@echo "        Install all requirements in the active environment."
	@echo "    build"
	@echo "        Build distribution to publish on PyPI and remove old."
	@echo "    docs"
	@echo "        Convert markdown docs to rst for PyPI."
	@echo "    publish"
	@echo "        Make all pre-checks and publish to PyPI."
	@echo "    test"
	@echo "        Run all the tests."
	@echo "    lint"
	@echo "        Run the linters."
	@echo "    cov"
	@echo "        Run all the tests and check the coverage."
	@echo "    update"
	@echo "        Update requirements."
	@echo "    upload"
	@echo "        Upload distribution to PyPI."

deps:
	@echo "Installing requirements..."
	pip install -r requirements.txt
	@echo "Done"

build:
	@echo "Making distribution..."
	rm -f dist/*
	python setup.py sdist
	@echo "Done"

docs:
	@echo "Generating documentation..."
	pandoc --from=markdown --to=rst --output=README.rst README.md
	@echo "Done"

publish:
	@echo "Publish package to PyPI..."
	make test
	make lint
	make cov
	make docs
	make build
	make upload
	@echo "Done"

test:
	@echo "Running tests..."
	python -m pytest tests/
	@echo "Done"

lint:
	@echo "Running linters..."
	python -m pylint quizler/ tests/
	@echo "Done"

cov:
	@echo "Running tests and checking coverage..."
	python -m pytest --cov=./ tests/
	@echo "Done"

update:
	@echo "Updating requirements..."
	pur -r requirements.txt
	@echo "Done"

upload:
	@echo "Upload distribution to PyPI..."
	twine upload dist/*
	@echo "Done"
