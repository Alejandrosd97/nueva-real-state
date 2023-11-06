from django.db import models

# Create your models here.


from django.db import models
from houses.models import House
from django.utils import timezone
from django.conf import settings

# Create your models here.

class ChatMessage (models.Model): 
    message_body = models.CharField(max_length=1000)
    message_author = models.ForeignKey('ChatMessageAuthor', on_delete=models.CASCADE, related_name='author')
    message_receiver = models.ForeignKey('ChatMessageAuthor', on_delete=models.CASCADE, related_name='receiver')
    date_posted = models.DateField(default=timezone.now)
    conversation = models.ForeignKey('ChatConversation', on_delete=models.CASCADE)

    def __str__(self):
        return f'Message: {self.message_body}'



class ChatConversation (models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    owner = models.ForeignKey('ChatMessageAuthor', on_delete=models.CASCADE, related_name='owner')
    customer = models.ForeignKey('ChatMessageAuthor', on_delete=models.CASCADE, related_name='customer')
    last_modified = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Property: {self.house.address}, owner: {self.owner}, customer: {self.customer}, last modified: {self.last_modified}'


class ChatMessageAuthor (models.Model):
    user_author = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_owner = models.BooleanField(default= False)

    def __str__(self):
        return f'Name: {self.user_author.first_name} {self.user_author.last_name}'

 



