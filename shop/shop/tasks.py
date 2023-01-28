from celery import shared_task
from .models import Order
import requests


@shared_task()
def send_order(order_id):
    order = Order.objects.get(id=order_id)
    order_item = order.orderitem_set.all()

    body = {
        'user': order.user.username,
        'user_email': order.user.email,
        'city': order.city,
        'address': order.address,
        'order_id_in_shop': order.id,
        'order_item': [
                {
                    'book_store': item.book.id,
                    'quantity': item.quantity
                } for item in order_item
        ]
    }

    r = requests.post('http://sklad:8001/order/', json=body)

    pass
