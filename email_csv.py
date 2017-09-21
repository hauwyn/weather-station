#!/usr/bin/env python
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
fromaddr = "hummingbirdtechwd@gmail.com"
toaddr = "cauwangyan@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Weather data from *** Farm"

collect_date = datetime.today()
collect_date = collect_date.strftime("%Y-%m-%d")

body = 'Hello,\n\nToday is '+collect_date+'. This is weather data from *** Farm. \n\n Have a nice day!'
msg.attach(MIMEText(body, 'plain'))
attachment = open("/home/pi/weather_data/all_weather.csv", "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename=Weather data "+collect_date+".csv")
#If Pi run a pyhton script, '.csv' is necessary to ensure the format! Otherwise, the output will be txt file!
msg.attach(part)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "hummingbird02684")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()