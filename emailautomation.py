from email.message import EmailMessage
import ssl
import smtplib




def mail_sender(from_name,to_name):
    em = EmailMessage()
    em['From'] = from_name
    em['To'] = to_name
    subject = 'New Python project'
    body = """
    testing mail sending program
    """

    em['Subject'] = subject
    em.set_content(body)

    email_password = '<enter email password generated from google two step verification>'

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    print("mail sent to ",to_name)

if __name__ == "__main__":
    print("mail called")
    email_sender = '<enter sender email address>'
    email_receiver = ['<receivers email address>', '<receivers email address>']

    for reciever in email_receiver:
        print(reciever)

        mail_sender(email_sender,reciever)
