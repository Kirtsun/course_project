from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Book(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    id_in_sklad = models.IntegerField()


class Order(models.Model):
    CART = 'CART'
    ORDERED = 'ORDERED'
    SUCCESS = 'SUCCESS'
    FAIL = 'FAIL'
    ORDER_CHOICES = [
        (CART, 'CART'),
        (ORDERED, 'ORDERED'),
        (SUCCESS, 'SUCCESS'),
        (FAIL, FAIL),
    ]
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=ORDER_CHOICES, default=CART, max_length=8)
    delivery_address = models.CharField(max_length=150)

