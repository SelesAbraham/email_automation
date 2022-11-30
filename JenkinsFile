pipeline {
    agent any
    triggers {
        //testing every 5 mins
        cron (*/5 * * * *)
        // every saturday at 8:00am
        // cron(59 7 * * 6)
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
