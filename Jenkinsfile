pipeline {
  agent any
  stages {
    stage('Check Python Version') {
      steps {
        bat 'py --version'
      }
    }
    stage('Build Script') {
      steps {
        bat 'py send_email.py -s %SENDER_EMAIL% -p %SENDER_PASSWORD% -r %RECEIVER_EMAIL% -su "%SUBJECT%" -rn "%RECEIVER_NAME%" -sn "%SENDER_NAME%" -m "%MESSAGE%"'
      }
    }
  }
}
