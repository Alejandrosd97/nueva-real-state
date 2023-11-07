from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .models import ChatConversation, ChatMessage, ChatMessageAuthor
from houses.models import House

# Create your views here.


User = get_user_model()

@login_required
def chat_page(request):
    user_watching = ChatMessageAuthor.objects.filter(user_author = request.user).first()
    if user_watching.is_owner:
        conversations = ChatConversation.objects.filter(owner=user_watching).order_by('-last_modified').all()
        
    else: 
        conversations = ChatConversation.objects.filter(customer=user_watching).order_by('-last_modified').all()
    

    
    return render(request, 'main_chat.html', {'conversations':conversations,
    'user_watching': user_watching})

@login_required
def chat_detail(request, conv_id):

    # GET ALL CONVERSATIONS
    user_watching = ChatMessageAuthor.objects.filter(user_author = request.user).first()
    if user_watching.is_owner:
        conversations = ChatConversation.objects.filter(owner=user_watching).order_by('-last_modified').all()
        
    else: 
        conversations = ChatConversation.objects.filter(customer=user_watching).order_by('-last_modified').all()
    current_conversation = conversations.filter(id=conv_id).first()
    other_convs = conversations.exclude(house= current_conversation.house,
                                        customer =current_conversation.customer, 
                                        owner= current_conversation.owner)
    if current_conversation:
        messages = current_conversation.chatmessage_set.all()
    else:
        messages= {}

    print(current_conversation)
    
    return render(request, 'chat_detail.html', {'conversations':other_convs, 'current_conversation':current_conversation,
    'user_watching': user_watching, 'messages': messages})





@login_required
def delete_conversation(request, conv_id):
    conversation_to_delete = ChatConversation.objects.filter(id=conv_id).first()
    conversation_to_delete.delete()

    return redirect('chat_page')


@login_required
def send_message(request, conv_id):
    conversation = ChatConversation.objects.filter(id=conv_id).first()
    author_message = ChatMessageAuthor.objects.filter(user_author = request.user).first()

    if author_message == conversation.owner:
        receiver = conversation.customer
    else:
        receiver = conversation.owner

    if request.POST:
       
        mensaje = ChatMessage(
            message_body = request.POST['message'],
            message_author = author_message,
            message_receiver = receiver,
            conversation = conversation
        )

        mensaje.save()
        conversation.last_modified = mensaje.date_posted
        conversation.save()

    return redirect('chat_page')

   

