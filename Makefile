help:
	@echo "    test"
	@echo "        Run all the tests."
	@echo "    requirements"
	@echo "        Install all requirements in the active environment."
	@echo "    docs"
	@echo "        Convert markdown docs to rst for PyPI."

test:
	@echo "Running tests..."
	python -m pytest tests/
	@echo "Done"

requirements:
	@echo "Installing requirements..."
	pip install -r requirements.txt
	@echo "Done"

docs:
	pandoc --from=markdown --to=rst --output=README.rst README.md
