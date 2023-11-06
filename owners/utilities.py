from django.contrib.auth import get_user_model
from django.core.mail import send_mail, EmailMessage
from django.conf import settings




def send_lower_price_email(emails, house):
    subject = 'Lower price'
    message = f'The house {house}, has dropped its price, it is now {house.price}'
    mensaje = EmailMessage(subject, message, settings.EMAIL_HOST_USER, to=emails)
    mensaje.send()

 