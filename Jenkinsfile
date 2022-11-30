pipeline {
  agent any
  triggers {
    cron('59 7 * * 6')
  }
  stages {
    stage('Check Python Version') {
      steps {
        bat 'python --version'
      }
    }
    stage('Build Script') {
      steps {
        bat 'python send_email.py'
      }
    }
  }
}
