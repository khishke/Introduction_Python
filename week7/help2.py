import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

me = "py4econ@gmail.com"
you = "sugarkhuu.radnaa@email.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you

text = MIMEText('<img src="cid:image1">', 'html')
msg.attach(text)

image = MIMEImage(open(r'C:\Users\sugarkhuu\Documents\python\repo\email-templates\2\images\image1.jpg', 'rb').read())

# Define the image's ID as referenced in the HTML body above
image.add_header('Content-ID', '<image1>')
msg.attach(image)


config ={}
config["From"] = "py4econ@gmail.com"
config["PASSWORD"] = "CaSaDa1!"
config["To"] = "sugarkhuu.radnaa@gmail.com"

s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.login(config["From"], config["PASSWORD"])
s.sendmail(config["From"], config["To"], msg.as_string())


# s.sendmail(config["From"], config["To"], msg.as_string())

# s = smtplib.SMTP('localhost')
# s.sendmail(from_addr, to_addr, msg.as_string())
s.quit()