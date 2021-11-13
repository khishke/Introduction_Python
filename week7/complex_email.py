### Email templates 
# https://colorlib.com/wp/responsive-html-email-templates/#free-email-templates
# https://github.com/ColorlibHQ/email-templates

### 
# https://stackoverflow.com/questions/920910/sending-multipart-html-emails-which-contain-embedded-images
# https://www.pauldesalvo.com/sending-an-html-formatted-email-with-attachments-through-gmail-using-python/


import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

import config # config.py file with info/credentials

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = config.From
msg['To'] = config.To # ", ".join(recipients)

# =============================================================================
# # Create the body of the message (a plain-text and an HTML version).
# text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
# html = """\
# <html>
#   <head></head>
#   <body>
#     <p>Hi!<br>
#        How are you?<br>
#        Here is the <a href="http://www.python.org">link</a> you wanted.
#     </p>
#   </body>
# </html>
# """
# 
# part1 = MIMEText(text, 'plain')
# msg.attach(part1)
# =============================================================================


# Record the MIME types of both parts - text/plain and text/html.
html = open(r"C:\Users\sugarkhuu\Documents\python\repo\email-templates\2\index.html")
part1 = MIMEText(html.read(), 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)

# take image files
image1 = MIMEImage(open(r'C:\Users\sugarkhuu\Documents\python\repo\email-templates\2\images\about.jpg', 'rb').read())
image2 = MIMEImage(open(r'C:\Users\sugarkhuu\Documents\python\repo\email-templates\2\images\blog-1.jpg', 'rb').read())
image3 = MIMEImage(open(r'C:\Users\sugarkhuu\Documents\python\repo\email-templates\2\images\blog-2.jpg', 'rb').read())
image4 = MIMEImage(open(r'C:\Users\sugarkhuu\Documents\python\repo\email-templates\2\images\person_1.jpg', 'rb').read())
image5 = MIMEImage(open(r'C:\Users\sugarkhuu\Documents\python\repo\email-templates\2\images\person_2.jpg', 'rb').read())
image6 = MIMEImage(open(r'C:\Users\sugarkhuu\Documents\python\repo\email-templates\2\images\person_3.jpg', 'rb').read())
image7 = MIMEImage(open(r'C:\Users\sugarkhuu\Documents\python\repo\email-templates\2\images\work-1.jpg', 'rb').read())
image8 = MIMEImage(open(r'C:\Users\sugarkhuu\Documents\python\repo\email-templates\2\images\work-2.jpg', 'rb').read())
image9 = MIMEImage(open(r'C:\Users\sugarkhuu\Documents\python\repo\email-templates\2\images\work-3.jpg', 'rb').read())
image10 = MIMEImage(open(r'C:\Users\sugarkhuu\Documents\python\repo\email-templates\2\images\work-4.jpg', 'rb').read())
image11 = MIMEImage(open(r'C:\Users\sugarkhuu\Documents\python\repo\email-templates\2\images\work-5.jpg', 'rb').read())
image12 = MIMEImage(open(r'C:\Users\sugarkhuu\Documents\python\repo\email-templates\2\images\work-6.jpg', 'rb').read())
image13 = MIMEImage(open(r'C:\Users\sugarkhuu\Documents\python\repo\email-templates\2\images\work-7.jpg', 'rb').read())
image14 = MIMEImage(open(r'C:\Users\sugarkhuu\Documents\python\repo\email-templates\2\images\work-8.jpg', 'rb').read())
image15 = MIMEImage(open(r'C:\Users\sugarkhuu\Documents\python\repo\email-templates\2\images\bg_1.jpg', 'rb').read())
image16 = MIMEImage(open(r'C:\Users\sugarkhuu\Documents\python\repo\email-templates\2\images\bg_2.jpg', 'rb').read())
image17 = MIMEImage(open(r'C:\Users\sugarkhuu\Documents\python\repo\email-templates\2\images\002-play-button.png', 'rb').read())


# Define the image's ID as referenced in the HTML body above
image1.add_header('Content-ID', '<about>')
msg.attach(image1)
image2.add_header('Content-ID', '<blog-1>')
msg.attach(image2)
image3.add_header('Content-ID', '<blog-2>')
msg.attach(image3)
image4.add_header('Content-ID', '<person_1>')
msg.attach(image4)
image5.add_header('Content-ID', '<person_2>')
msg.attach(image5)
image6.add_header('Content-ID', '<person_3>')
msg.attach(image6)
image7.add_header('Content-ID', '<work-1>')
msg.attach(image7)
image8.add_header('Content-ID', '<work-2>')
msg.attach(image8)
image9.add_header('Content-ID', '<work-3>')
msg.attach(image9)
image10.add_header('Content-ID', '<work-4>')
msg.attach(image10)
image11.add_header('Content-ID', '<work-5>')
msg.attach(image11)
image12.add_header('Content-ID', '<work-6>')
msg.attach(image12)
image13.add_header('Content-ID', '<work-7>')
msg.attach(image13)
image14.add_header('Content-ID', '<work-8>')
msg.attach(image14)
image15.add_header('Content-ID', '<bg_1>')
msg.attach(image15)
image16.add_header('Content-ID', '<bg_2>')
msg.attach(image16)
image17.add_header('Content-ID', '<002-play-button>')
msg.attach(image17)

# Adding attachments
attachment = MIMEApplication(open('note.docx', "rb").read(), _subtype="txt")
attachment.add_header('Content-Disposition','attachment', filename='note.docx')
msg.attach(attachment)

attachment = MIMEApplication(open('note.txt', "rb").read(), _subtype="txt")
attachment.add_header('Content-Disposition','attachment', filename='note.txt')
msg.attach(attachment)

attachment = MIMEApplication(open('note.xlsx', "rb").read(), _subtype="txt")
attachment.add_header('Content-Disposition','attachment', filename='note.xlsx')
msg.attach(attachment)
    
# Send the message via Gmail SMTP server.
s = smtplib.SMTP('smtp.gmail.com', 587)

s.ehlo()
s.starttls()
s.login(config.From, config.PASSWORD)

# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.

s.sendmail(msg["From"], msg["To"], msg.as_string())
s.quit()
