from django.shortcuts import render, redirect
from django.urls import reverse
from conversations.models import ChatMessageAuthor
from houses.models import House, City, HousePictures, Threshold_price
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import authenticate, login as dj_login, logout, get_user_model
from django.contrib.auth.hashers import check_password
from .forms import UserRegisterForm, SellingHouseForm, HouseImagesForm, UpdateHouseForm, UserLoginForm
from django.core.mail import send_mail, EmailMessage
from django.http import JsonResponse
from .utilities import send_lower_price_email



# Create your views here.

User = get_user_model()

@login_required
def selling_page (request):
    house_form = SellingHouseForm()
    
    if request.method == 'POST':
        house_form = SellingHouseForm(request.POST)
        city = request.POST['city'].lower()
        if City.objects.filter(city_name = city).exists():
            city_exists = City.objects.filter(city_name= city).first()
        
        else:
            city_exists = City(city_name = city)
            city_exists.save()

        images = request.FILES.getlist('image')

        if house_form.is_valid():
            new_house = house_form.save(commit=False)
            new_house.city = city_exists
            new_house.owner = request.user

            #AÑADIR TYPE FORM
            new_house.save()
            images = request.FILES.getlist('image')
            for image in images:
                picture = HousePictures(
                    house = new_house,
                    file = image
                )
                picture.save()

            request.user.is_owner = True
            return redirect('home_page')
        

    return render(request, 'selling.html', {'house_form': house_form})



def register(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
           
            dj_login(request, user)

            new_chat_author = ChatMessageAuthor(user_author=user)
            new_chat_author.save()

            subject = 'Successfully registered '
            message =f"Dear {user.first_name}, Welcome to MyRealState! We are thrilled to have you as part of our home search community. As a registered member, you've taken the first step towards realizing your dreams of finding the perfect home. At MyRealState, we are committed to making your property search experience as straightforward and satisfying as possible.\n Kind regards"
            email= user.email
  
            mensaje = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
            try:
                mensaje.send()
            except: 
                print('error enviando emial')
           
            return redirect('home_page')

    if request.method == 'GET':
        form = UserRegisterForm()

    return render(request, 'register.html', {'form':form})



def login(request):
    form = UserLoginForm()
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect('home_page')
        else:
            print('no autenticado')
   

    return render(request, 'login.html', {'form': form})


    
@login_required
def my_properties (request):
    properties = House.objects.filter(owner= request.user)

    return render(request, 'my_properties.html', {'properties': properties})



@login_required
def edit_add(request, id):
    house = House.objects.filter(id=id).first()
    images = list(house.housepictures_set.all()) 
    tell_me = house.threshold_price_set.all()
    list_of_emails = []
    previous_price = house.price
    form = UpdateHouseForm( instance=house)


    if request.POST:
        form =UpdateHouseForm(request.POST, instance= house)
        if request.user == house.owner:
            if form.is_valid():    
                form.save()
                for price in tell_me:  
                    if house.price <= price.lower_than_price and house.price < previous_price:
                        list_of_emails.append(price.user.email)
                        
                send_lower_price_email(list_of_emails, house)           
                return redirect('my_properties')
           
    else:
        form = UpdateHouseForm(instance= house)

    return render(request, 'update_add.html', {'id':id, 'images':images, 'form': form})

@login_required
def remove_picture(request, id):
    picture = HousePictures.objects.filter(id=id).first()
    if picture.house.owner == request.user:
        picture.delete()
    
    return redirect('my_properties')


@login_required
def add_picture(request, id):
    house = House.objects.filter(id=id).first()
    if house.owner_id == request.user.id and request.POST:
        images = request.FILES.getlist('image')
        for image in images:
            picture = HousePictures(
                house = house,
                file = image
                )
            picture.save()
        house.price = request.POST.get('price')
        house.description = request.POST.get('description')
        house.save()
        
   
    
    return redirect('my_properties')
        

@login_required
def remove_add(request, id):
    house_to_remove = House.objects.filter(id=id).first()
    if house_to_remove.owner_id == request.user.id:  
        house_to_remove.delete()


    return redirect('my_properties')


@login_required
def logout_page(request):
    logout(request)
    return redirect('home_page')



@login_required
def lower_price(request, id):
    house= House.objects.filter(id=id).first()
    customer = request.user
    new_threshold = Threshold_price(
        house = house,
        user = customer,
        lower_than_price = request.POST['lower-price']
    )
    new_threshold.save()

    url = f'/houses_detail/{id}'
 
    return redirect(url)