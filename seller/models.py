from django.db import models

class Seller(models.Model):
    unique_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    langitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    wallet = models.CharField(max_length=255)
    total_get_products_count = models.IntegerField()
    stock = models.CharField(max_length=255)

class Category(models.Model):
    unique_id = models.CharField(max_length=255, primary_key=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name="children")
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    name_uzkr = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='category/', null=True, blank=True)

class Product(models.Model):
    unique_id = models.CharField(max_length=255, primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    name_uzkr = models.CharField(max_length=255)
    stock_in_warehouse = models.IntegerField() 
    selling_price = models.IntegerField()
    input_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_kombo = models.BooleanField(default=True)


class Kombo_products(models.Model):
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    kombo_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    product_id = models.ManyToManyField(Product, blank=True, null=True)
    amount = models.IntegerField()

class Seller_wallet_log(models.Model):
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.IntegerField()
    is_take = models.BooleanField(default=True)