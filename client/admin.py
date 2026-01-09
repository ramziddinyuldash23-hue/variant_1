from django.contrib import admin
from .models import Client, Favourites, lead_status, tags
# Register your models here.
admin.site.register(Client)
admin.site.register(Favourites)
admin.site.register(lead_status)
admin.site.register(tags)