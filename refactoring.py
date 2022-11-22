import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart

class EmailProcessor():
    
    def __init__(self, login, password) -> None:
        self.GMAIL_SMTP = "smtp.gmail.com"
        self.GMAIL_IMAP = "imap.gmail.com"
        self.login = login
        self.password = password

    def send_message(self, send_to:list, message_subject:str, message_text:str) -> None:
        message = MIMEMultipart()
        message['From'] = self.login
        message['To'] = ', '.join(send_to)
        message['Subject'] = message_subject
        message.attach(MIMEText(message_text))
        message_session = smtplib.SMTP(self.GMAIL_SMTP, 587)
        message_session.ehlo()
        message_session.starttls()
        message_session.ehlo()
        message_session.login(self.login, self.password)
        message_session.sendmail(self.login, message_session, message_text.as_string())
        message_session.quit()

    def recieve_message(self, header=None, mail_folder='inbox'):     
        mailbox = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mailbox.login(self.login, self.password)
        mailbox.list()
        mailbox.select(mail_folder)
        _, message_data = mailbox.uid('search', None, f'(HEADER Subject "{header if header else "ALL"}")')
        try:
            latest_email_uid = message_data[0].split()[-1]
        except IndexError:
            return 'There are no letters with current header'
        _, message_data = mailbox.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = message_data[0][1]
        email_message = email.message_from_string(raw_email)
        mailbox.logout()
        return email_message

if __name__ == '__main__':
    recipients_list = ['vasya@email.com', 'petya@email.com']
    my_email = EmailProcessor('login@gmail.com', 'qwerty')
    my_email.send_message(send_to=recipients_list, message_subject='Very important message', message_text='test_message')
    my_email.recieve_message()