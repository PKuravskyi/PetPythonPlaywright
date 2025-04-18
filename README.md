# Practice test automation with Python and Playwright

### How to run tests locally:

1. Install all dependencies: `pip install -r requirements.txt`
2. Run tests: `python -m pytest`

#### You can also specify additional arguments during run:

1. Run in parallel: `-n <num_of_parallel_tests>`
2. Browsers to run on: `--browser=<browser_name>`. Possible values: `chromium`, `firefox`, `webkit`
3. Specific tests, examples:
    1. Test suite: `tests/ui`
    2. Test file: `tests/ui/register_user_test.py`
    3. Single test: `tests/ui/arts_test.py::test_art_can_be_added_to_basket`
    4. Tests with tags: `-m smoke`, `-m 'smoke and not wip'`, `-m 'not wip'` etc. To see the full list of tags refer
       to [pytest.ini > markers](pytest.ini)

Example command to run only working smoke UI tests in parallel:  
`python -m pytest -n 5 -m 'smoke and not wip' tests/ui`

### How to run tests inside of docker container:

1. Build image: `docker-compose build test-runner`
2. Run tests: `docker-compose run --rm test-runner xvfb-run pytest`  
   Refer
   to [You can also specify additional arguments during run](#you-can-also-specify-additional-arguments-during-run)
   section to see the list of available arguments during run.

Example docker-compose command to run only working smoke UI tests in parallel:  
`docker-compose run --rm test-runner xvfb-run pytest -n 5 -m 'smoke and not wip' tests/ui`

### How to start Jenkins UI:

1. Build image: `docker-compose build jenkins-ui`
2. Run the container: `docker-compose up -d jenkins`
3. Navigate to http://localhost:8080/. Username: `admin`. Password: `f84ae56e48094de7ab9b5943572d31d5`

### How to see test results:

Option 1: After tests are executed you can see allure results by running command: ```allure serve allure-results```   
Option 2: You can go to the GitHub pages of this repository (https://pkuravskyi.github.io/PetPythonPlaywright/) which
has the allure results from the latest GitHub Action run on `main` branch

### How to Lint code errors:

Run `pylint **/*.py` command to lint all code errors

### How to update libraries/dependencies:

1. Update dependencies to the latest compatible versions: `pip-compile`
2. Install new versions locally`pip install -r requirements.txt`

