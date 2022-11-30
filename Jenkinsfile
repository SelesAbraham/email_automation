pipeline {
  agent any
  triggers {
    cron('59 7 * * 6')
  }
  stages {
    stage('Check Python Version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('Build Script') {
      steps {
        sh 'python3 send_email.py'
      }
    }
  }
}
