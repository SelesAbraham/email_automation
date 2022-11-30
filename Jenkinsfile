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
      steps {2
        bat 'py send_email.py -s %SENDER_EMAIL% -p %SENDER_PASSWORD% -r %RECEIVER_EMAIL% -su "%SUBJECT%" -rn "%RECEIVER_NAME%" -sn "%SENDER_NAME%" -m "%MESSAGE%"'
      }
    }
  }
}
