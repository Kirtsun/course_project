from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class BookItem(models.Model):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    RACK = [
        (A, 'A'),
        (B, 'B'),
        (C, 'C'),
        (D, 'D')
    ]
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rack = models.CharField(choices=RACK, max_length=1)
    place = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.book.title


class Order(models.Model):
    IN_WORK = 'IN_WORK'
    SUCCESS = 'SUCCESS'
    FAIL = 'FAIL'
    ORDER_CHOICES = [
        (IN_WORK, 'IN_WORK'),
        (SUCCESS, 'SUCCESS'),
        (FAIL, 'FAIL'),
    ]
    user = models.CharField(max_length=100)
    user_email = models.EmailField()
    status = models.CharField(choices=ORDER_CHOICES, max_length=10, default=IN_WORK)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    order_id_in_shop = models.PositiveIntegerField()

    def __str__(self):
        return f'Order Id {str(self.id)}, User {self.user}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book_store = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    book_items = models.ManyToManyField(BookItem)

    def __str__(self):
        return f'{self.book_store.title} x {self.quantity}'


# class OrderItemBookItem(models.Model):
#     class OrderItemBookItem(models.Model):
#         order_item = models.ForeignKey(OrderItem)
#         book_item = models.ForeignKey(BookItem)
#
#     def __str__(self):
#         return f'Order Item Book Item Id {str(self.id)}'

