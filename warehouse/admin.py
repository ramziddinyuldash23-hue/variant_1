from django.contrib import admin
from .models import warehouse, warehouse_group, warehouse_group_topic
# Register your models here.
admin.site.register(warehouse)
admin.site.register(warehouse_group)
admin.site.register(warehouse_group_topic)
