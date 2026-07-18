pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'playwright',
                url: 'https://github.com/praveenatnv666/GitDemo.git'
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
