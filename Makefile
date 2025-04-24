.PHONY: install-deps test-all test-smoke test-docker-all test-docker-smoke update-deps lint allure jenkins

# Install deps with Poetry
install-deps:
	poetry install

# Run all tests
test-all:
	poetry run pytest

# Run smoke tests
test-smoke:
	poetry run pytest -m 'smoke'

# Run all tests inside Docker
test-docker-all:
	docker-compose run --rm test-runner xvfb-run pytest

# Run smoke tests inside Docker
test-docker-smoke:
	docker-compose run --rm test-runner xvfb-run pytest -m 'smoke'

# Update all deps via Poetry
update-deps:
	poetry update

# Lint with Pylint
lint:
	poetry run pylint **/*.py

# Serve Allure report
allure:
	allure serve allure-results

# Start Jenkins locally
jenkins:
	docker-compose up -d jenkins
