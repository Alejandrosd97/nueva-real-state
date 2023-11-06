from django.urls import path
from. import views


urlpatterns = [
    path('chat/', views.chat_page , name='chat_page'),
    path('chat/<int:conv_id>', views.chat_detail, name='chat_detail'),
    #path('chat_conv/<int:conv_id>', views.chat_conversation, name='chat_conversation'),
    path('chat_conv/delete/<int:conv_id>', views.delete_conversation, name='delete_conversation'),
    path('send_message/<int:conv_id>', views.send_message, name='send_message'),
    #path('other/<int:id>', views.other_conversations, name='other_conversations'),

]