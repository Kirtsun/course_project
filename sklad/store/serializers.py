from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Book, BookItem, Order, OrderItem, OrderItemBookItem

User = get_user_model()


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['order', 'book_store', 'quantity']
        read_only_fields = ['order', ]


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    order_item = OrderItemSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = ['user', 'user_email', 'status', 'city', 'address', 'order_id_in_shop', 'order_item']

    def create(self, validated_data):
        order = Order.objects.create(user=validated_data['user'],
                                     user_email=validated_data['user_email'],
                                     city=validated_data['city'],
                                     address=validated_data['address'],
                                     order_id_in_shop=validated_data['order_id_in_shop'])
        batch = [OrderItem(book_store=item['book_store'], order=order,
                           quantity=item['quantity']) for item in validated_data['order_item']]
        order.orderitem_set.bulk_create(batch)
        return order

