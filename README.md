# Email Automation using Jenkins pipeline

The goal of this project is to send automatic email updates to the recipient every Saturday morning. 
In this repository, there exist two files: 

- Python script which is used to send email using SMTP server
- JenkinsFile which is used to pass the parameters and trigger the Python script

Note: I have setup a Gmail test account, for Gmail SMTP server to work, it is important to enable [security settings](https://support.google.com/accounts/answer/185833) in your gmail account. 

## How to use?

1. Logon to Jenkins, click on `New Item`, enter Jenkins Job name and then select `Pipeline` and click on ok
2. Select the Job, go to `Configure`, click `Advanced Project Options`fron the left panel. On the right under `Pipeline Definition`, select `Pipeline Script from SCM`, then in the `Repositories` section paste the [respoitory URL](https://github.com/SelesAbraham/email_automation). Selct SCM as Git. Then under `Branches to build`, mention the branch name, in this scenario the branch is `main`. The default script path is `Jekinsfile`. Click `Save`.
3. Go to the Job that you just created, click on `Build Parameters`, fill the required entries ( e.g.: Sender & Receiver Email ID and Password), the rest has default values and then trigger the Job. 

>NOTE: Don't forget to add your credential details in `Global Credential` under `Manage Credentials` in Jenkins and replace ID mentioned in the [Jenkinsfile](https://github.com/SelesAbraham/email_automation/blob/main/Jenkinsfile#L23) with the ID of your credential stored in Jenkins. In this repository I have my test Gmail account credential ID.

Once the Build is successful, the email recipient should receive an email. 

Automatic trigger of build: In this repository, [Cron Job](https://github.com/SelesAbraham/email_automation/blob/main/Jenkinsfile#L4) is set to schedule every Saturday at 8:00AM. 
