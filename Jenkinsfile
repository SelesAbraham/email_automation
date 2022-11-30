pipeline {
  agent any
  triggers {
    cron('59 7 * * 6')
  }
  stages {
    stage('Check Python Version') {
      steps {
        bat 'py --version'
      }
    }
    stage('Build Script') {
      steps {
        bat 'py send_email.py -s params.SENDER_EMAIL -p params.SENDER_PASSWORD -r params.RECEIVER_EMAIL -su params.SUBJECT -rn params.RECEIVER_NAME -sn params.SENDER_NAME -m params.MESSAGE'
      }
    }
  }
}
