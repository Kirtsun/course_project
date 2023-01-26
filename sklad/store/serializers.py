from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Book, BookItem, Order, OrderItem, OrderItemBookItem

User = get_user_model()


class BookSerializer(serializers.HyperlinkedModelSerializer):
    bookitem = serializers.HyperlinkedRelatedField(many=True, view_name='bookitem-detail', source='bookitem_set',
                                                   queryset=BookItem.objects.all())

    class Meta:
        model = Book
        fields = ['url', 'id', 'title', 'price', 'bookitem']


class BookItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BookItem
        fields = ['url', 'id', 'place', 'book']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    order_item = serializers.HyperlinkedRelatedField(many=True, view_name='orderitem-detail', source='orderitem_set',
                                                     queryset=OrderItem.objects.all())

    class Meta:
        model = Order
        fields = ['url', 'id', 'user', 'user_email', 'status', 'city', 'address', 'order_id_in_shop', 'order_item']


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    bookitem = serializers.HyperlinkedRelatedField(many=True, view_name='orderitembookitem-detail',
                                                   read_only=True)

    class Meta:
        model = OrderItem
        fields = ['url', 'id', 'quantity', 'book_store', 'order', 'bookitem']


class OrderItemBookItemSerializer(serializers.HyperlinkedModelSerializer):
    order_item = serializers.HyperlinkedRelatedField(many=True, view_name='orderitem-detail',
                                                     read_only=True)
    book_item = serializers.HyperlinkedRelatedField(many=True, view_name='bookitem-detail',
                                                    read_only=True)

    class Meta:
        model = OrderItemBookItem
        fields = ['url', 'id', 'order_item', 'book_item']

