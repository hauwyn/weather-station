import smtplib
import mimetypes
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

emailfrom = "hummingbirdtechwd@gmail.com"
emailto = "cauwangyan@gmail.com"
fileToSend = "/home/pi/Desktop/weather1.db"
username = "hummingbirdtechwd@gmail.com"
password = "hummingbird02684"

msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] = emailto
msg["Subject"] = "Weather data from *** Farm"
msg.preamble = "This is weather data from ***. Have a nice day!"

ctype, encoding = mimetypes.guess_type(fileToSend)
if ctype is None or encoding is not None:
    ctype = "application/octet-stream"

maintype, subtype = ctype.split("/", 1)
if maintype == "text":
    fp = open(fileToSend)
    # Note: we should handle calculating the charset
    attachment = MIMEText(fp.read(), _subtype=subtype)
    fp.close()
else:
    fp = open(fileToSend, "rb")
    attachment = MIMEBase(maintype, subtype)
    attachment.set_payload(fp.read())
    fp.close()
    encoders.encode_base64(attachment)

record_time = datetime.today()
record_time = record_time.strftime("%Y-%m-%d %H:%M:%S")
attachment.add_header("Content-Disposition", "attachment", filename="weather data "+ record_time + ".db")
msg.attach(attachment)

server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(username,password)
server.sendmail(emailfrom, emailto, msg.as_string())
server.quit()