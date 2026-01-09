from django.db import models

# Create your models here.
class tags(models.Model):
    unique_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class lead_status(models.Model):
    unique_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    ststus_id = models.IntegerField()

class Client(models.Model):
    unique_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    order_count = models.IntegerField(default=0)
    return_products_count = models.IntegerField(default=0)
    tags = models.ManyToManyField(tags, blank=True)
    lead_id = models.IntegerField()
    lead_status_id = models.ForeignKey(lead_status, on_delete=models.CASCADE, null=True, blank=True)
    trek_number = models.CharField(max_length=100, null=True, blank=True)
    custom_number = models.CharField(max_length=100, null=True, blank=True)
    from_where = models.CharField(max_length=100, null=True, blank=True)

class Favourites(models.Model):
    unique_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    quanity = models.IntegerField(default=1)
    price = models.IntegerField()