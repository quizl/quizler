help:
	@echo "    test"
	@echo "        Run all the tests."
	@echo "    deps"
	@echo "        Install all requirements in the active environment."
	@echo "    update"
	@echo "        Update requirements."
	@echo "    docs"
	@echo "        Convert markdown docs to rst for PyPI."

test:
	@echo "Running tests..."
	python -m pytest tests/
	@echo "Done"

deps:
	@echo "Installing requirements..."
	pip install -r requirements.txt
	@echo "Done"

update:
	@echo "Updating pur..."
	pip install -U pur
	@echo "Updating requirements..."
	pur -r requirements.txt
	@echo "Done"

docs:
	pandoc --from=markdown --to=rst --output=README.rst README.md
