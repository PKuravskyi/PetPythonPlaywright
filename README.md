# Practice test automation with Python and Playwright

## Prerequisites:

[Install Poetry](https://python-poetry.org/docs/#installation) on your local machine  
[Install Make](https://www.google.com/search?q=how+to+install+%22Make%22) on your local machine (optional)

### How to run tests locally:

1. Install all dependencies: `poetry install`
2. Make sure you are using poetry venv: `poetry env activate`. You can also set poetry interpreter in your IDE.
3. Run [Shopping Store app](bin) on your local machine
4. Run tests: `python -m pytest`

#### Optional test arguments:

1. Run in parallel: `-n <num_of_parallel_tests>`
2. Browsers to run on: `--browser <browser_name>`. Possible values: `chromium`, `firefox`, `webkit`. Default value:
   `chromium`
3. Specific tests, examples:
    1. Test suite: `tests/ui`
    2. Test file: `tests/ui/register_user_test.py`
    3. Single test: `tests/ui/arts_test.py::test_art_can_be_added_to_basket`
    4. Tests with tags: `-m smoke`, `-m 'smoke and not wip'`, `-m 'not wip'` etc. To see the full list of tags refer
       to _markers_ in [pyproject.toml](https://github.com/PKuravskyi/PetPythonPlaywright/blob/main/pyproject.toml#L28)

Example command to run only working smoke UI tests in firefox in parallel:  
`python -m pytest -n 5 --browser firefox -m 'smoke and not wip' tests/ui`

### How to run tests inside of docker container:

1. Build image: `docker-compose build test-runner`
2. Run tests: `docker-compose run --rm test-runner xvfb-run pytest`  
   Refer
   to [Optional test arguments](#optional-test-arguments)
   section to see the list of available arguments during run.

Example docker-compose command to run only working smoke UI tests in parallel:  
`docker-compose run --rm test-runner xvfb-run pytest -n 5 -m 'smoke and not wip' tests/ui`

### How to run tests inside of GitHub:

1. Go to the **Actions** tab in GitHub.
2. Find and select the **"Run Playwright Tests"** workflow.
3. Click the **"Run workflow"** button.
4. Fill in the inputs:

| Input          | Description                                                                                | Example                                                                    |
|:---------------|:-------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------|
| **Branch**     | Name of the branch to test.                                                                | `main`, `feature/my-branch`                                                |
| **Browsers**   | Browsers to run tests on (comma-separated). Valid values: `chromium`, `firefox`, `webkit`. | `chromium`, `chromium, firefox`                                            |
| **Tags**       | *(Optional)* Pytest markers to select tests.                                               | `smoke and ui`, `not wip`                                                  |
| **Tests list** | *(Optional)* Specific tests or folders to run. Separate by commas or spaces.               | `ui/login_test.py`, `ui/login_test.py ui/arts_test.py::test_add_to_basket` |
| **Threads**    | How many tests to run in parallel.                                                         | `5`                                                                        |

> **Note**:
> - If **Tests list** is empty, all tests will be run.
> - Tests paths should be relative to the `tests/` folder.

5. Press **"Run workflow"** and wait for it to finish.
6. Allure reports will be uploaded as artifacts.

### How to start Jenkins UI:

1. Build image: `docker-compose build jenkins-ui`
2. Run the container: `docker-compose up -d jenkins`
3. Navigate to http://localhost:8080/. Username: `admin`. Password: `f84ae56e48094de7ab9b5943572d31d5`

### How to see test results:

Option 1: After tests are executed locally you can see allure results by running command:
`allure serve allure-results`   
Option 2: After tests are executed in GitHub Actions you can download Allure reports artifact, extract and see allure
results by running command: `allure serve allure-results`

### How to Lint code errors:

1. Pylint: run `pylint **/*.py` command to lint all code. Or with Make `make pylint`
2. Mypy: run `mypy --explicit-package-bases .` command to lint all code. Or with Make `make mypy`

### How to update libraries/dependencies (Poetry):

1. Install all dependencies from `pyproject.toml`:  
   `poetry install`

2. Add a new dependency (without changing others):  
   `poetry add <package_name>`

3. Update a specific package to the latest version:  
   `poetry update <package_name>`

4. Update **all** dependencies to latest allowed versions:  
   `poetry update`

### How to run Make commands:

1. Have "Make" installed on your local machine, refer to [prerequisites](#prerequisites)
2. Go through the [Makefile](Makefile) to see the list of available commands
3. Run the command, example: `make test-docker-all`

### How to autoformat code locally:

1. Autoformat everything in a project: `black .`. You can also specify custom path or files you want to autoformat
