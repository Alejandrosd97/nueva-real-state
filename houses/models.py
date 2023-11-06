from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

from django.db import models
from django.conf import settings

from owners.models import CustomUser



# Create your models here.



class House (models.Model):
    RENT_BUY_CHOICES = [( 'rent' ,'Rent') , ('buy', 'Buy')]
    PROPERTY_TYPES = [('Residential', 'Residential'), ('Commercial', 'Commercial'), ('Countryside', 'Countryside'), ('Apartments', 'Apartments')]

    title = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    type = models.CharField(max_length=11 , choices= PROPERTY_TYPES, default='Residential')
    price = models.FloatField()
    description = models.TextField(blank=True)
    rooms  = models.IntegerField()
    garage = models.BooleanField()
    bathrooms = models.IntegerField()
    m2 = models.IntegerField()
    rent_or_sell = models.CharField(max_length=4 , choices= RENT_BUY_CHOICES, default='buy')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner')
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add ='True')
    last_modified = models.DateTimeField(auto_now ='True')
    likes =models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_author')
    longitude = models.DecimalField(max_digits=12, decimal_places=8)
    latitude = models.DecimalField(max_digits=12, decimal_places=8)

    #lower_price = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='interested_in_lower_price')

    def __str__(self):
        return self.title

class Threshold_price(models.Model):
    house = models.ForeignKey('House', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='customer')
    lower_than_price = models.IntegerField()

    def __str__(self):
        return f'Customer: {self.user}, House: {self.house}, Price:{self.lower_than_price}$' 

class HousePictures(models.Model):
    file = CloudinaryField()
    house = models.ForeignKey('House', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.file}, {self.house}'



class City (models.Model): 
    city_name= models.CharField(max_length= 50)
    longitude = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)

    def __str__(self):
        return self.city_name

# class Like (models.Model):
#     user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='like_author')
#     house = ForeignKey('House', on_delete=models.CASCADE, related_name='liked_house')
#     date_liked =  models.DateTimeField(auto_now_add='True')
