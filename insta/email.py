from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(username,receiver):
    # Creating message subject and sender
    subject = 'Welcome to  Instagram Clone app'
    sender = 'maestrowebsites@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/useremail.txt',{"username": username})
    html_content = render_to_string('email/useremail.html',{"username": username})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()