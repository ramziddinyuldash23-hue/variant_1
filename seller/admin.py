from django.contrib import admin
from .models import Seller, Category, Product, Kombo_products, Seller_wallet_log

# Register your models here.
admin.site.register(Seller)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Kombo_products)
admin.site.register(Seller_wallet_log)