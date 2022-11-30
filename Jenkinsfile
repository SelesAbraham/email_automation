pipeline {
  agent any
  triggers {
    cron('59 7 * * 6')
    }
    stages {
      stage('Python Version') {
        steps {
          sh 'python3 --version'
          echo "Done"
        }
      }
      stage('Run Script') {
        steps {
          sh 'python3 send_email.py'
        }
      }
    }
}
