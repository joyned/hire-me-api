import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.model.email.EmailMessage import EmailMessage
from app.utils.resource import ResourceUtil


def send_email(email_message: EmailMessage):
    mime_message = MIMEMultipart('alternative')

    mime_message['Subject'] = email_message.subject
    mime_message['From'] = email_message.from_email
    mime_message['To'] = email_message.to

    email_body = email_message.get_body()

    body = MIMEText(email_body, 'html')

    mime_message.attach(body)

    try:
        sender = smtplib.SMTP(get_mail_property('host'), get_mail_property('port'))
        sender.sendmail(mime_message['From'], mime_message['To'], mime_message.as_string())
        sender.quit()
    except Exception as e:
        raise RuntimeError(e)


def get_mail_property(property):
    mail_config = ResourceUtil.get_resource_file('mail_config.yml')
    return mail_config['mail'][property]
