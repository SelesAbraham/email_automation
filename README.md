# Email Automation using Jenkins pipeline

In this repository, there exist two files: 

- Python script which is used to send email using SMTP server .
- JenkinsFile which is used to pass the parameters and trigger the Python script

Note: I have setup a Gmail test account, for Gmail SMTP to work, it is important to enable some [security settings](https://support.google.com/accounts/answer/185833) in your gmail account

## How to use?

1. Logon to Jenkins, click on `New Item`, enter Jenkins Job name and then select `Pipeline` and click on ok
2. Select the job, go to `Configure`, select `Advanced Project Options`. Here under `Pipeline Definition`, select `Pipeline Script from SCM`, then in the `Repositories` section paste the [respoitory URL](https://github.com/SelesAbraham/email_automation). Then under `Branches to build`, put the branch name, in this scenario the branch is `main`. The default script path is `Jekinsfile`. Click `Save`.
3. Now select `General` section which is on the left panel. On the right side, tick `This project is parameterized`, and `Add Parameters` as follows:
    - Select String parameter and name it `SENDER_EMAIL`
    - Select Password paramter and name it `SENDER_PASSWORD`
    - Select String Parameter and name it `RECEIVER_EMAIL`
Similary for `SUBJECT`, `RECEIVER_NAME`, `SENDER_NAME`, `MESSAGE` as String parameter

How to execute Jenkings job?:

1. Manual: Go to `Build with parameters`, fill in all the required values and trigger the job. As soon as the buid is successful, you should receive en email.
2. Automatic: In order to trigger the jenkins job periodically, I have installed a plugin named `Parameterized Scheduler`. Under Build Trigger section, select `Build periodically with parameters`. Then in the Schedule one could define the cron-like schdeule.

For e.g: Schedule a job every Saturday at 8:00AM

```bash
H 8 * * 6 %SENDER_EMAIL=<put_gmail_id>;SENDER_PASSWORD=<put gmail_app_password>;RECEIVER_EMAIL=<email_id>;SUBJECT=Weekly Maintenance;RECEIVER_NAME=Monitoring Team;SENDER_NAME=SRE Team;MESSAGE=System XYZ has weekly maintenance on Saturday from 14:00 until 17:00 CET
```
