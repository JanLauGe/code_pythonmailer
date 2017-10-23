
def send_email(sender, password, recipient, subject, message):
    """Sends email via gmail. 
    <Allow less secure apps> needs to be enabled in google account settings"""
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    
    # Format message
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    body = message
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()

    # Send as email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender, password)
        server.sendmail(sender, recipient, text)
        server.close()
        print('successfully sent the mail')
    except:
        print('failed to send mail')
        
        

sender = 'someemail'
recipient = 'someemail'
subject = 'testsubject'
message = 'Hi there, this is a robot test message.'

send_email(sender, recipient, subject, message)


