# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage
from string import Template
from pathlib import Path
html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Ewane Elvis'
email['to'] = 'domemail@gmail.com'
email['subject'] = 'You won a 1,000,0000 dollars!'

email.set_content(html.substitute({'name':'pythonboy'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ewanelvis@gmail.com', 'zunqyuimarnaahjl')
    smtp.send_message(email)
    print('all good boss')


