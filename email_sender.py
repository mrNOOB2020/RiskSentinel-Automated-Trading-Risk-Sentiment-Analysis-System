import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_email(report_file, sender, password, receiver):
  
    msg = MIMEMultipart()
    msg['Subject'] = 'Daily Trading Report'
    msg['From'] = sender
    msg['To'] = receiver

 
    with open(report_file, "r", encoding="utf-8") as f:
        html = f.read()

    
    msg.attach(MIMEText(html, 'html'))

    
    with open("equity.png", "rb") as img_file:
        img_data = img_file.read()
    image = MIMEImage(img_data, name="equity.png")
    image.add_header('Content-ID', '<equity>')
    msg.attach(image)

   
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        server.send_message(msg)
