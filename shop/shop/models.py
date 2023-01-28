from django.db import models
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django_lifecycle import LifecycleModel, hook, AFTER_UPDATE


User = get_user_model()


class Book(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    id_in_sklad = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Order(LifecycleModel):
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=ORDER_CHOICES, default=CART, max_length=8)
    city = models.CharField(max_length=150)
    address = models.CharField(max_length=150)

    @hook(AFTER_UPDATE, when="status", was="*", is_now='SUCCESS')
    def on_status(self):
        send_mail('Order in a bookstore', f'You order have a new status: "{self.status}", wait for the delivery'
                                          f' of the purchase', 'bookstore@gmail.com',
                  [self.user_id.email],
                  fail_silently=False)

    @hook(AFTER_UPDATE, when="status", was="*", is_now='FAIL')
    def on_status(self):
        send_mail('Order in a bookstore', f'Yuo order have a new status "{self.status}". The store administration'
                                          f' will contact you shortly.', 'bookstore@gmail.com',
                  [self.user_id.email],
                  fail_silently=False)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return self.price * self.quantity

    def __str__(self):
        return self.book.title


