from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Book, BookItem, Order, OrderItem, OrderItemBookItem

User = get_user_model()


class BookSerializer(serializers.HyperlinkedModelSerializer):
    book = serializers.HyperlinkedRelatedField(many=True, view_name='book-detail', source="book_set",
                                               queryset=BookItem.objects.all(), format='JSON')

    class Meta:
        model = Book
        fields = ['url', 'id', 'title', 'price', 'book']


class BookItemSerializer(serializers.HyperlinkedModelSerializer):
    orderitem_bookitem = serializers.HyperlinkedRelatedField(many=True, view_name='order-item-book-item',
                                                             queryset=OrderItemBookItem.objects.all())

    class Meta:
        model = BookItem
        fields = ['url', 'id', 'place', 'orderitem_bookitem']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    order_item = serializers.HyperlinkedRelatedField(many=True, view_name='order-item',
                                                     queryset=OrderItem.objects.all())

    class Meta:
        model = Order
        fields = ['url', 'id', 'user', 'user_email', 'status', 'city', 'address', 'order_id_in_shop', 'order_item']


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    order = serializers.HyperlinkedRelatedField(many=True, view_name='order', source='order_set',
                                                queryset=Order.objects.all())
    book_store = serializers.HyperlinkedRelatedField(many=True, view_name='book', source='book_set',
                                                     queryset=Book.objects.all())

    class Meta:
        model = OrderItem
        fields = ['url', 'id', 'quantity', 'order', 'book_store']


class OrderItemBookItemSerializer(serializers.HyperlinkedModelSerializer):
    order_item = serializers.HyperlinkedRelatedField(many=True, view_name='order-item',
                                                     queryset=OrderItem.objects.all())
    book_item = serializers.HyperlinkedRelatedField(many=True, view_name='book-item',
                                                    queryset=BookItem.objects.all())

    class Meta:
        moder = OrderItemBookItem
        fields = ['url', 'id', 'order_item', 'book_item']

