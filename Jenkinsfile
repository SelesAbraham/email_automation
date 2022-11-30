pipeline {
  agent any
  triggers {
    cron('59 7 * * 6')
  }
  stages {
    stage('Check Python Version') {
      steps {
        bat 'python3 --version'
      }
    }
    stage('Build Script') {
      steps {
        bat 'python3 send_email.py'
      }
    }
  }
}
