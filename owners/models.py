from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin,AbstractBaseUser

# Create your models here.

class CustomManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone_number, password, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email= email, first_name= first_name,
                         last_name= last_name, phone_number=phone_number, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, phone_number, password, **other_fields):
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)

        return self.create_user(email, first_name, last_name, phone_number, password, **other_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=80)
    phone_number = models.IntegerField( unique=True, null=True)
    is_owner = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','phone_number']

    objects = CustomManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'





