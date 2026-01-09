from django.db import models

# Create your models here.
class Delivery(models.Model):
    unique_id = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    wallet = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    order_count = models.IntegerField(default=0)
    working_status = models.BooleanField(default=True)

class Dilivery_wallet_log(models.Model):
    class Type(models.TextChoices):
        CASH = 'CASH', 'Cash'
        CART = 'CART', 'Cart'
    unique_id = models.CharField(max_length=100, unique=True)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    amount_cash = models.DecimalField(max_digits=10, decimal_places=2)
    amount_cart = models.DecimalField(max_digits=10, decimal_places=2)
    is_taken = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Dilivery_workdays(models.Model):
    delivery_id = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    work_time = models.CharField(max_length=100)
    work_day = models.ManyToManyField('Dilivery_days')

class Dilivery_days(models.Model):
    unique_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=50)

class Dilivery_addresses(models.Model):
    unique_id = models.CharField(max_length=100, unique=True)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    addresses_name = models.CharField(max_length=200)
    langtude = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Dilivery_group(models.Model):
    unique_id = models.CharField(max_length=100, unique=True)
    dilivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    group_id = models.CharField(max_length=100)
    group_name = models.CharField(max_length=100)

class Dilivery_group_topic(models.Model):
    unique_id = models.CharField(max_length=100, unique=True)
    dilivery_group = models.ForeignKey(Dilivery_group, on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=100)
    message = models.TextField()
    topic_id = models.CharField(max_length=100)
