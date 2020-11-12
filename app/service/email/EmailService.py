import os
import smtplib
import sys
from email.mime.image import MIMEImage

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

    root = os.path.abspath(os.path.dirname(sys.argv[0]))

    fp = open(os.path.join(root, 'resource/img', 'logo.png'), 'rb')
    msg_image = MIMEImage(fp.read())
    fp.close()

    body = MIMEText(email_body, 'html')

    mime_message.attach(body)

    msg_image.add_header('Content-ID', '<header-logo>')
    mime_message.attach(msg_image)

    try:
        sender = smtplib.SMTP(get_mail_property('host'), get_mail_property('port'))
        sender.starttls()
        sender.login(get_mail_property('user'), get_mail_property('pwd'))
        sender.sendmail(mime_message['From'], mime_message['To'], mime_message.as_string())
        sender.quit()
    except Exception as e:
        raise RuntimeError(e)


def get_mail_property(property):
    mail_config = ResourceUtil.get_resource_file('mail_config.yml')
    return mail_config['mail'][property]
