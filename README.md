# Practice test automation with Python and Selenium

## How to run tests locally:
1. `pip install -r requirements.txt`
2. `python -m pytest`  
**NOTE:**: you can also specify additional parameters during run:
   1. Run in parallel - `-n <num_of_parallel_tests>`
   2. Add html reporting - `--template=html1/index.html --report=test-reports/report.html`
   3. Add allure reporting - `-alluredir allure-results`
