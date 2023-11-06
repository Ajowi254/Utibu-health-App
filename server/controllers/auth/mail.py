# mail.py
import os
import sendgrid
from sendgrid.helpers.mail import Mail

def send_email(email, token):
    message = Mail(
        from_email='from_email@example.com',
        to_emails=email,
        subject='Confirm Your Email',
        html_content=f'<a href="http://localhost:5000/confirm/{token}">Confirm your email</a>')
    try:
        sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
