import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart

class EmailProcessor:
    
    def __init__(self) -> None:
        self.GMAIL_SMTP = "smtp.gmail.com"
        self.GMAIL_IMAP = "imap.gmail.com"
        self.login = 'login@gmail.com'
        self.password = 'qwerty'
        self.subject = 'Subject'
        self.recipients = ['vasya@email.com', 'petya@email.com']
        self.message = 'Message'
        self.header = None

    def send_message(self, send_from:str, send_to:list, message_subject:str = None):
        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = ', '.join(send_to)
        msg['Subject'] = message_subject
        msg.attach(MIMEText(self.message))
        ms = smtplib.SMTP(self.GMAIL_SMTP, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, msg.as_string())
        ms.quit()

    def recieve_message(self, criterion, mail_folder='inbox'):     
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select(mail_folder)
        criterion = f'(HEADER Subject "{self.header if self.header else "ALL"}")'
        _, data = mail.uid('search', None, criterion)
        try:
            latest_email_uid = data[0].split()[-1]
        except IndexError:
            return 'There are no letters with current header'
        _, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        return email_message

if __name__ == '__main__':
    email_handler = EmailProcessor