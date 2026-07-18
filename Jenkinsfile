pipeline {

    agent any
    options {
        disableConcurrentBuilds()
    }
    
    triggers {
    cron('H/30 * * * *')
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Packages') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Install Browsers') {
            steps {
                bat 'playwright install'
            }
        }

        stage('Run Script') {
            steps {
                bat 'python practice.py'
            }
        }

    }

}
