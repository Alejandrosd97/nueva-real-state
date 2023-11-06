from houses.models import House, HousePictures
from owners.models import CustomUser

from django import forms
from django.contrib.auth.forms import UserCreationForm




class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder' : 'First Name', 'autofocus': True, 'class':'form-control'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder' : 'Last Name', 'class':'form-control'}))
    email = forms.CharField(widget = forms.EmailInput(attrs={'placeholder' : 'Email','class':'form-control'}))
    phone_number = forms.CharField(widget = forms.TextInput(attrs={'placeholder' : 'Phone Number', 'class':'form-control'}))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder' : 'Password', 'class':'form-control'}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder' : 'Repeat your password', 'class':'form-control'}))

    class Meta():
        model= CustomUser
        fields=['first_name', 'last_name', 'phone_number', 'email', 'password1', 'password2']


class UserLoginForm(forms.Form):
    email = forms.CharField(widget = forms.EmailInput(attrs={'placeholder': 'Email', 'class':'form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'form-control'}))


class MessageForm (forms.Form):
    message = forms.Textarea()


class SellingHouseForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':9,'cols':40, 'maxlength': 500, 'class':'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'id':'hidden-input-address', 'class':'form-control', 'type':'hidden', 'value':' '' '}), label='' )    
    latitude = forms.DecimalField(widget=forms.TextInput(attrs={ 'id':'hidden-input-lat', 'type':'hidden', 'value':' '' '}), label='' )
    longitude = forms.DecimalField(widget=forms.TextInput(attrs={ 'id':'hidden-input-long', 'type':'hidden', 'value':' '' '}), label='' )
    title = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control'}))
    price = forms.IntegerField(widget = forms.TextInput(attrs={ 'class':'form-control'}))
    rooms = forms.IntegerField(widget = forms.TextInput(attrs={'class':'form-control'}))
    bathrooms = forms.IntegerField(widget = forms.TextInput(attrs={'class':'form-control'}))
    m2 = forms.IntegerField(widget = forms.TextInput(attrs={'class':'form-control'}))
    RENT_BUY_CHOICES = [( 'rent' ,'For rent') , ('buy', 'For sale')]
    rent_or_sell = forms.CharField(widget = forms.Select(attrs={'class':'form-select'},choices=RENT_BUY_CHOICES))
    PROPERTY_TYPES = [('Residential', 'Residential'), ('Commercial', 'Commercial'), ('Countryside', 'Countryside'), ('Apartments', 'Apartments')]
    type = forms.CharField(widget = forms.Select(attrs={'class':'form-select'},choices= PROPERTY_TYPES))

    garage = forms.BooleanField(widget= forms.CheckboxInput(attrs={'class': 'form-check-input'}))


    class Meta:
        model= House
        fields = ['title', 'address', 'latitude', 'longitude', 'type', 'price', 'rooms', 'garage', 'bathrooms', 'm2',
            'rent_or_sell', 'description']


class HouseImagesForm(forms.ModelForm):
    class Meta():
        model = HousePictures
        fields = ['file']


class UpdateHouseForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':9,'cols':40}))
    price = forms.IntegerField(widget = forms.TextInput(attrs={ 'class':'form-control'}))
    rooms = forms.IntegerField(widget = forms.TextInput(attrs={'class':'form-control'}))
    bathrooms = forms.IntegerField(widget = forms.TextInput(attrs={'class':'form-control'}))
    m2 = forms.IntegerField(widget = forms.TextInput(attrs={'class':'form-control'}))
    RENT_BUY_CHOICES = [( 'rent' ,'Rent') , ('buy', 'Buy')]
    rent_or_sell = forms.CharField(widget = forms.Select(attrs={'class':'form-select'},choices=RENT_BUY_CHOICES))
    garage = forms.BooleanField(widget= forms.CheckboxInput(attrs={'class': 'form-check-input'}))
   
    

    class Meta:
        model= House
        fields = [ 'price', 'rooms', 'garage', 'bathrooms', 'm2','rent_or_sell', 'description']  
