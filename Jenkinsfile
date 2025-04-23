#!groovy

List threads = ['5', '4', '3', '2', '1']
def failedTests = []

pipeline {
    agent any

    options {
        buildDiscarder(logRotator(daysToKeepStr: '30', numToKeepStr: '10', artifactDaysToKeepStr: '7'))
        timeout(time: 1, unit: 'HOURS')
        timestamps()
        skipDefaultCheckout(true)
    }

    parameters {
        gitParameter(
            name: 'BRANCH',
            branchFilter: '.*',
            defaultValue: 'origin/main',
            type: 'PT_BRANCH',
            sortMode: 'ASCENDING_SMART',
            selectedValue: 'DEFAULT'
        )

        extendedChoice(
                name: 'BROWSERS',
                defaultValue: 'chromium',
                description: 'Playwright browsers to use. Choose at least one.',
                multiSelectDelimiter: ',',
                saveJSONParameterToFile: false,
                type: 'PT_CHECKBOX',
                value: 'chromium, firefox, webkit',
                visibleItemCount: 3
        )

        string(
            name: 'TAGS',
            description: '''Run tests with specific tags.\nYou can select multiple tags by using 'and' word. Use 'not' word to exclude test with specified tag.\nExamples:
smoke and ui
smoke and not wip
not wip
            ''',
            trim: true
        )

        text(
            name: 'TESTS_LIST',
            description: '''List of tests to run. You can specify folder with tests, one test file, or one specific test from suite. Each item should begin on new line.\nExamples:
ui/
ui/register_user_test.py
ui/arts_test.py::test_art_can_be_removed_from_basket'''
        )

        choice(
            name: 'THREADS',
            choices: threads,
            description: 'Choose how many tests will be executed in parallel.'
        )
    }

    stages {
        stage('Validate Parameters') {
            steps {
                script {
                    if (params.BROWSERS.trim() == '') {
                            error 'No projects selected. Please choose at least one project.'
                    }
                }
            }
        }

        // Don't use 'Lightweight checkout' on Jenkins UI in order for this to work
        stage('Clone repository') {
            steps {
                git branch: params.BRANCH.replaceFirst(/^origin\//, ''), url: 'https://github.com/PKuravskyi/PetPythonPlaywright.git'
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    sh '''
                      poetry install --no-interaction --no-ansi
                      poetry run python -m playwright install --with-deps
                    '''
                }
            }
        }

        stage('Start Shopping Store App') {
            steps {
                sh '''
                    chmod +x './ShoppingStoreApp/shopping-store-linux-amd64'
                    ./ShoppingStoreApp/shopping-store-linux-amd64 > /dev/null 2>&1 &
                '''
            }
        }

        stage('Run tests') {
            steps {
                script {
                    def browsers = params.BROWSERS
                                         .split(',')
                                         .collect { it.trim() }
                                         .collect { "--browser ${it}" }
                                         .join(' ')

                    def testCommand = "poetry run xvfb-run pytest -n ${params.THREADS} ${browsers}"

                    if (params.TESTS_LIST?.trim()) {
                        def tests = params.TESTS_LIST
                                        .split('\n')
                                        .collect { it.trim().replace('\\', '/') }
                                        .join(' ')
                        testCommand += " tests/${tests}"
                    }

                    if (params.TAGS?.trim()) {
                        testCommand += " -m \"${params.TAGS}\""
                    }

                    sh testCommand
                }
            }
        }
    }

    post {
        always {
            allure includeProperties: false, results: [[path: 'allure-results']]
        }
    }
}

def sendEmailToRequestor() {
    emailext(recipientProviders: [requestor()],
    subject: "${currentBuild.projectName} - Build # ${currentBuild.id} - ${currentBuild.result}!",
    body: "${currentBuild.projectName} - Build # ${currentBuild.id} - ${currentBuild.result}: Check console output at ${currentBuild.absoluteUrl} to view the results.")
}
