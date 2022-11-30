pipeline {
    agent any
    triggers {
        cron (*/5 * * * *)
    }
    stages {
        stage('Clone repository') {
            steps {
                checkout scm
                echo "Checkout successful"
            }
        stage('Run Script') {
            steps {
                sh 'python3 send_email.py'
            }
        }
        }
    }
}
