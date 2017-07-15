help:
	@echo "    test"
	@echo "        Run all the tests."
	@echo "    requirements"
	@echo "        Install all requirements in the active environment."

test:
	@echo "Running tests..."
	python -m pytest tests/
	@echo "Done"

requirements:
	@echo "Installing requirements..."
	pip install -r requirements.txt
	@echo "Done"
