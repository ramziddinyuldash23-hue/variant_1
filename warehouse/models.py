from django.db import models

# Create your models here.
class warehouse(models.Model):
    unique_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    lanitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    total_products = models.IntegerField()

class warehouse_group(models.Model):
    unique_id = models.AutoField(primary_key=True)
    warehouse = models.ForeignKey(warehouse, on_delete=models.CASCADE)
    group_id = models.IntegerField()
    group_name = models.CharField(max_length=255)

class warehouse_group_topic(models.Model):
    unique_id = models.AutoField(primary_key=True)
    warehouse_group = models.ForeignKey(warehouse_group, on_delete=models.CASCADE)
    topic_id = models.IntegerField()
    topic_name = models.CharField(max_length=255)
    messeage_id = models.IntegerField()