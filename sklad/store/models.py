from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class BookItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    place = models.CharField(max_length=150, default='in store')


class Order(models.Model):
    IN_WORK = 'IN_WORK'
    SUCCESS = 'SUCCESS'
    FAIL = 'FAIL'
    ORDER_CHOICES = [
        (IN_WORK, 'IN_WORK'),
        (SUCCESS, 'SUCCESS'),
        (FAIL, FAIL),
    ]
    user = models.CharField(max_length=100)
    user_email = models.EmailField()
    status = models.CharField(choices=ORDER_CHOICES, max_length=10)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    order_id_in_shop = models.PositiveIntegerField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book_store = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class OrderItemBookItem(models.Model):
    order_item = models.ManyToManyField(OrderItem)
    book_item = models.ManyToManyField(BookItem)



