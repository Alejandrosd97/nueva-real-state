from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from owners.models import CustomUser
from .models import House
from owners.forms import UserRegisterForm

from django.contrib.auth import get_user_model
from houses.models import City, House
from owners.forms import UserRegisterForm

from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from conversations.models import ChatConversation, ChatMessage, ChatMessageAuthor

from django.core.mail import send_mail, EmailMessage
from django.conf import settings


# Create your views here.

User = get_user_model()

def home(request):
   searched = request.GET.get('city-searched')
   rent_or_buy = request.GET.get('rent-or-buy')
   if searched is not None and searched !='':
      
      city = City.objects.filter(city_name=searched.lower()).first()
      if city:
         city_id = city.id
         return redirect('houses_per_city', id=city_id, availability=rent_or_buy)

      else:
         new_city = City(city_name = searched.lower())
         new_city.save()
         city_id = new_city.id
      return redirect('houses_per_city', id=city_id, availability=rent_or_buy)
   
      
   return render(request, template_name='home.html') 



def houses_per_city(request, availability, id):
   
   
   if request.GET.get('max_price'):
      max_price= request.GET.get('max_price')
      print(max_price)
   else:
      max_price = 9999999999
   
   if request.GET.get('min_rooms'):
      min_rooms= request.GET.get('rooms')
      print(min_rooms)
   else:
      min_rooms = 1

   if request.GET.get('min_m2'):
      min_m2= request.GET.get('min_m2')
      print(min_m2)
   else:
      min_m2= 1

   if request.GET.get('availability'):
      availability= request.GET.get('availability')
   
   city_name = City.objects.filter(id=id).first()
   
   city_houses = House.objects.filter(price__lte=max_price,
    rooms__gte= min_rooms, m2__gte=min_m2, city=id,
         rent_or_sell = availability).all().order_by('-date_added')
   
  

   p = Paginator(city_houses, 5)
   page = request.GET.get('page')
   houses = p.get_page(page)      

   #print(houses)
      
      
   return render(request, 'houses_per_city.html',{'city_houses':houses,'id':id,
    'rent_or_buy':availability, 'city_name': city_name, 'number_of_houses': city_houses })


def house_detail(request, id):
   house = House.objects.filter(id=id).first()
   form = UserRegisterForm()
   users_liked = list(house.likes.all())
   is_liked = False
   if request.user in users_liked:
      is_liked = True
   
   has_sent_message =False

   if request.user.is_authenticated:
      customer = ChatMessageAuthor.objects.filter(user_author = request.user).first()
      already_sent = ChatConversation.objects.filter(house=house, customer= customer).first()
      if already_sent:
         has_sent_message=True


   images = house.housepictures_set.all()
   if images:
      first_image = images.first()
      other_images= images.exclude(house=first_image.house, file=first_image.file)

   else:
      first_image=None
      other_images= []

   
      

   return render(request, 'house_detail.html', {'house':house, 'form': form,
    'first_image': first_image, 'is_liked': is_liked, 'other_images':other_images,
    'message_sent': has_sent_message})


@login_required
def like_page(request, id):
   house = House.objects.filter(id=id).first()
   house.likes.add(request.user)
   city_id = house.city.id
  
   return redirect('houses_per_city', id=city_id , availability='buy')


@login_required
def dislike_page(request, id):
   house = House.objects.filter(id=id).first()
   house.likes.remove(request.user)

   return redirect('favourites_page')


@login_required
def favourites(request):
   favourites = request.user.like_author.all()
   print(favourites)

   return render(request, 'favourites.html', {'favourites': favourites})

 



@login_required
def contact_owner_form(request, id):

   house = House.objects.filter(id=id).first()

   if request.method == 'POST':
      if request.user.is_authenticated == False:
         print('no autenticado')
      else:
         message = request.POST['message']
         
  
      sender = ChatMessageAuthor.objects.filter(user_author = request.user).first()
      
      if not sender:
         sender = ChatMessageAuthor(
            user_author = request.user
            )
         sender.save()
         
      receiver = ChatMessageAuthor.objects.filter(user_author = house.owner).first()
      
      if not receiver:
         receiver = ChatMessageAuthor(
               user_author = house.owner,
               is_owner = True
            )
         receiver.save()

      already_contacted= ChatConversation.objects.filter(house = house, 
         owner = receiver,customer = sender).first()
      
      if already_contacted == None:
         conversation = ChatConversation(
            house = house,
            owner = receiver,
            customer = sender
         )
         print('hola', conversation, house )
         conversation.save()
      
      #SI YA SE HA ENVIADO UN MENSAJE AL DUEÑO QUITAR EL FROMULARIO
       
         message = ChatMessage(
            message_body = request.POST['message'],
            message_author = sender,
            message_receiver = receiver,
            conversation = conversation
         )

         message.save()
      else:
         print('ya hay una conversacion')

   return redirect('house_detail', id=id)




