# Practice test automation with Python and Selenium

### How to run tests locally:

1. `pip install -r requirements.txt`
2. `python -m pytest`  
   **NOTE:**: you can also specify additional parameters during run:
    1. Run in parallel - `-n <num_of_parallel_tests>`
    2. Add html reporting - `--template=html1/index.html --report=test-reports/report.html`

### How to see test results

Option 1: After tests are executed you can see allure results by running command: ```allure serve allure-results```   
Option 2: You can go to the GitHub pages of this repository (https://pkuravskyi.github.io/PetPythonPlaywright/) which
has the allure results from the latest run

### How to Lint code errors

Use `pylint **/*.py` command to lint all code errors
