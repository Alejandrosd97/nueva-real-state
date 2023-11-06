from django.contrib import admin
from .models import ChatConversation, ChatMessage, ChatMessageAuthor
# Register your models here.


admin.site.register([ChatConversation, ChatMessage, ChatMessageAuthor])