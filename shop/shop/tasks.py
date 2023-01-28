from celery import shared_task
from .models import Order, Book
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
    if r.status_code == 200:
        order.status = 'ORDERED'
    else:
        send_order.apply_async((order.id,), countdown=60)
    pass


@shared_task()
def sync_book():
    r = requests.get('http://sklad:8001/book/')
    if r.status_code == 200:
        res = r.json()
        for i in res:
            Book.objects.update_or_create(
                         title=i['title'],
                         price=i['price'],
                         id_in_sklad=i['id'],
                         quantity=len(i['book']))

    pass
