from django.db import models

# Create your models here.

class Order(models.Model):
    class PaymentType(models.TextChoices):
        CASH = 'CASH', 'Cash'
        CARD = 'CARD', 'Card'
        ONLINE = 'ONLINE', 'Online Payment'

    class OrderStatus(models.TextChoices):
        CREATED = 'CREATED', 'Created'
        PROCESS_OF_CONFIRMATION = 'PROCESS_OF_CONFIRMATION', 'Process of Confirmation'
        PREPARING_ORDER = 'PREPARING_ORDER', 'Preparing Order'
        DELIVERED_TOCARGO = 'DELIVERED_TOCARGO', 'Delivered to Cargo'
        DELIVERED_TO_CUSTOMER = 'DELIVERED_TO_CUSTOMER', 'Delivered to Customer'
        RETURNED = 'RETURNED', 'Returned'
        ORDER_AT_CARGO = 'ORDER_AT_CARGO', 'Order at Cargo'
        DELIVERED_TO_REGION = 'DELIVERED_TO_REGION', 'Delivered to Region'
        DELIVER_TAKE_TO_DELIVERY = 'DELIVER_TAKE_TO_DELIVERY', 'Deliver Take to Delivery'
        DELIVER_CANT_CALL_CUSTOMER = 'DELIVER_CANT_CALL_CUSTOMER', 'Deliver Cant Call Customer'

    class Order_canceled(models.TextChoices):
        ORDER_FROM_CARGO = 'ORDER_FROM_CARGO', 'Order from Cargo'
        DELIRING_FROM_CARGO_TO_MAIN = 'DELIRING_FROM_CARGO', 'Deliring from Cargo'
        DELIVERED_FROM_MAIN = 'DELIVERED_FROM_MAIN', 'Delivered from Main'
        DELIVER_TOOK_ORDER_FROM_MAIN_CARGO = 'DELIVER_TOOK_ORDER_FROM_MAIN_CARGO', 'Deliver Took Order from Main Cargo'
        DEVERED = 'DEVERED', 'Devered'

    unique_id = models.AutoField(primary_key=True)
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE)
    delivery = models.ForeignKey('dilivery.Delivery', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    payment_type = models.CharField(max_length=50)
    is_send_cargo = models.BooleanField(default=False)
    cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE, null=True, blank=True) 

class Cargo(models.Model):
    unique_id = models.CharField(primary_key=True)
    name = models.CharField(max_length=255)
    cargo_id = models.IntegerField()
    cargo_status = models.CharField(max_length=50)

class Order_products(models.Model):
    unique_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
