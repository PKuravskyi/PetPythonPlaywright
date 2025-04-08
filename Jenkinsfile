#!groovy

List workers = ['5', '4', '3', '2', '1']
def failedTests = []

pipeline {
    agent any

    options {
        buildDiscarder(logRotator(daysToKeepStr: '30', numToKeepStr: '10', artifactDaysToKeepStr: '7'))
        timeout(time: 1, unit: 'HOURS')
        timestamps()
    }

    environment {
        CI = true
        STUDENT_USERNAME = credentials('STUDENT_USERNAME')
        STUDENT_PASSWORD = credentials('STUDENT_PASSWORD')
    }

    parameters {
        gitParameter(
            name: 'BRANCH',
            branchFilter: '.*',
            defaultValue: 'main',
            type: 'PT_BRANCH'
        )

        extendedChoice(
                name: 'BROWSERS',
                defaultValue: 'Google Chrome',
                description: 'Playwright browsers to use. Choose at least one.',
                multiSelectDelimiter: ',',
                saveJSONParameterToFile: false,
                type: 'PT_CHECKBOX',
                value: 'Google Chrome, Microsoft Edge, Mobile Chrome, Mobile Safari',
                visibleItemCount: 5
        )

        string(
            name: 'TAGS_TO_INCLUDE',
            description: 'Run tests that include specific tags. Example:\n@smoke @ui',
            trim: true
        )

        string(
            name: 'TAGS_TO_EXCLUDE',
            description: 'Run tests that do not include specific tags. Example:\n@wip @flaky',
            trim: true
        )

        text(
            name: 'TESTS_LIST',
            description: '''List of tests to run. You can specify folder with tests, one test file, or one specific test from suite.
                \nEach item should begin on new line. Examples:
                \nui
                \nui/register_user_test.py
                \nui/arts_test.py:9
            ''' )

        choice(
            name: 'WORKERS',
            choices: workers,
            description: 'Choose how many tests will be executed in parallel.'
        )
    }

    stages {
        stage('Validate Parameters') {
            steps {
                script {
                    if (params.BROWSERS.trim() == '') {
                            error "No projects selected. Please choose at least one project."
                    }
                }
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    sh '''
                      pip install -r requirements.txt
                      playwright install --with-deps
                    '''
                }
            }
        }

        stage('Start Shopping Store App') {
            steps {
                sh '''
                    chmod +x './ShoppingStoreApp/shopping-store-linux-amd64'
                    ./ShoppingStoreApp/shopping-store-linux-amd64 &
                '''
            }
        }

        stage('Run tests') {
            steps {
                script {
                    def projects = getSelectedProjects()

                    def testCommand = 'pytest'

                    if (params.TESTS_LIST) {
                        def tests = params.TESTS_LIST
                                        .split('\n')
                                        .collect { it.trim().replace('\\', '/') }
                                        .join(' ')
                        testCommand += " tests/${tests}"
                    }

                    if (params.TAGS_TO_INCLUDE) {
                        testCommand += " --grep ${params.TAGS_TO_INCLUDE}"
                    }

                    if (params.TAGS_TO_EXCLUDE) {
                        testCommand += " --grep-invert ${params.TAGS_TO_EXCLUDE}"
                    }

                    testCommand += " --workers=${params.WORKERS} --project ${projects}"

                    sh 'xvfb-run pytest'
                }
            }
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}

def getSelectedProjects() {
    return params.BROWSERS
                 .split(',')
                 .collect { it.trim() }
                 .collect { "'${it}'" }
                 .join(' ')
}

def sendEmailToRequestor() {
    emailext(recipientProviders: [requestor()],
    subject: "${currentBuild.projectName} - Build # ${currentBuild.id} - ${currentBuild.result}!",
    body: "${currentBuild.projectName} - Build # ${currentBuild.id} - ${currentBuild.result}: Check console output at ${currentBuild.absoluteUrl} to view the results.")
}
