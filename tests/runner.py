import unittest
from os import environ


class TestResults(unittest.TestResult):

    def addError(self, test, err):
        super(TestResults, self).addError(test, err)  
        self.sendNotifications(test, err)

    def addFailure(self, test, err):
        super(TestResults, self).addFailure(test, err)
        self.sendNotifications(test, err)

    def getEnvironmentSetting(self, setting):
        return environ[setting]

    def splitStringByComma(self, string):
        return string.split(',')

    def sendNotifications(self, test, err):
        self.sendNotificationEmails(test, err)
        self.sendNotificationPhone(test, err)

    def sendNotificationEmails(self, test, err):
        send_email_notifications_addresses = self.getEnvironmentSetting('SEND_EMAIL_NOTIFICATIONS_TO')
        email_addresses = self.splitStringByComma(send_email_notifications_addresses)
        for email in email_addresses:
            self.sendNotificationEmail(email, test, err)

    def sendNotificationPhone(self, test, err):
        send_sms_notifications_phones = self.getEnvironmentSetting('SEND_SMS_NOTIFICATIONS_TO')
        phone_numbers = self.splitStringByComma(send_sms_notifications_phones)
        for phone_number in phone_numbers:
            self.sendNotificationSms(phone_number, test, err)

    def sendNotificationSms(self, phone_number, test, err):
        from twilio.rest import Client

        account_sid = self.getEnvironmentSetting('TWILIO_ACCOUNT_SID')
        auth_token  = self.getEnvironmentSetting('TWILIO_AUTH_TOKEN')
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to=phone_number, 
            from_=self.getEnvironmentSetting('TWILIO_PHONE_NUMBER'),
            body="Automated test failure! {}".format(test))

    def sendNotificationEmail(self, to_email, test, err):
        from sendgrid.helpers.mail import Email, Content, Mail
        import sendgrid

        client = sendgrid.SendGridAPIClient(apikey=self.getEnvironmentSetting('SENDGRID_API_KEY'))
        from_email = Email('testrunner@test.com')
        to_email = Email(to_email)
        subject = 'Automated tests failure'
        content = Content("text/plain", '{} \r\n {}'.format(test, err))
        mail = Mail(from_email, subject, to_email, content)
        response = client.client.mail.send.post(request_body=mail.get())        


if __name__ == '__main__':
    suite = unittest.TestSuite(
        unittest.TestLoader().discover('test_units')
    )
    results = TestResults()
    suite.run(results)


