from django.db.models.signals import post_save
from .models import ChatMessage
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.mail import send_mail, EmailMessage
from django.conf import settings




User = get_user_model()

@receiver(post_save, sender= ChatMessage)
def send_new_message_notice(sender, instance, **kwargs):
    message_receiver = instance.message_receiver
   
    subject = 'New Message'
    message = 'You have received a new message'
    author = message_receiver.user_author
    email= author.email
   
    mensaje = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
    try:
        mensaje.send()
    except: 
        print('error enviando emial')


