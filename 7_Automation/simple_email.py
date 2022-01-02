### Open the port 587
# https://www.tomshardware.com/news/how-to-open-firewall-ports-in-windows-10,36451.html

### Allow less secure app in Gmail
# https://www.google.com/settings/security/lesssecureapps
# Chrome - Account - Security - Less secure apps access

import os
print('Working directory at: ', os.getcwd())
# os.chdir(r'7_Automation')


import smtplib # to connect to email client
from email.mime.multipart import MIMEMultipart # managing email msg
from email.mime.text import MIMEText           # managing email msg
import pandas as pd
import config # config.py file with info/credentials
import logging



# mail content
msg = MIMEMultipart('alternative')
msg['Subject'] = "hello" #"hi %s and hi %s" %(15,20)
msg['From'] = config.From
msg['To'] = config.To # ", ".join(recipients)
msg['CC'] = "sugarkhuul@gmail.com"
msg['BCC'] = "sugarkhuu.radnaa@gmail.com"

text = "Hello, \n Өдрийн мэнд хүргэе. Best,\n Sugarkhuu"
part1 = MIMEText(text, 'plain')
msg.attach(part1)

# setup and login
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login(config.From, config.PASSWORD)

# print(logging.info('Just quit the mail client.') )

try:
    mail.sendmail(msg['From'], msg['To'] + ", " + msg['CC'] + ", "+ msg['BCC'], msg.as_string())
    print("Success: Email sent!")
except Exception as e:
    print(e)
    print("Email failed to send.")
  
mail.quit()

# logging.basicConfig(level=logging.INFO, file='sample.log')
# # logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# # logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
# print(logging.info('Just quit the mail client.'))
