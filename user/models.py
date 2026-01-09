from django.db import models

# Create your models here.

class User(models.Model):
    class role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        SUPER_ADMIN = 'SUPER_ADMIN', 'Super Admin'
        DELIVERY = 'DELIVERY', 'Delivery'
        MERCHANT = 'MERCHANT', 'Merchant'
        CLIENT = 'CLIENT', 'Client'
    unique_id = models.CharField(max_length=255, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    adress = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telegram = models.CharField(max_length=255)
    step = models.CharField(max_length=255)
    language = models.CharField(max_length=20) 

