pipeline {
  agent any
  parameters {
    string(name: 'SENDER_EMAIL', defaultValue: '', description: 'Enter sender email-id')
    password(name: 'SENDER_PASSWORD', defaultValue: 'SECRET', description:'Enter a password')
    string(name: 'RECEIVER_EMAIL', defaultValue: '', description: 'Enter recipients email id')
    string(name: 'SUBJECT', defaultValue: 'Weekly Maintenance', description: 'Enter subject of email')
    string(name: 'RECEIVER_NAME', defaultValue: 'Monitoring Team', description: 'To')
    string(name: 'SENDER_NAME', defaultValue: 'SRE Team', description: 'From')
    string(name: 'MESSAGE', defaultValue: 'Service XYZ has planned maintenance on Saturday from 14:00 till 17:00 CET', description: 'Enter content of email')
  }
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
