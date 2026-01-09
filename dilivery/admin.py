from django.contrib import admin
from .models import Delivery, Dilivery_wallet_log, Dilivery_workdays, Dilivery_days, Dilivery_addresses, Dilivery_group, Dilivery_group_topic
# Register your models here.
admin.site.register(Delivery)
admin.site.register(Dilivery_wallet_log)
admin.site.register(Dilivery_workdays)
admin.site.register(Dilivery_days)
admin.site.register(Dilivery_addresses)
admin.site.register(Dilivery_group)
admin.site.register(Dilivery_group_topic)
