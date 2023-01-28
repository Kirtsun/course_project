from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Book, BookItem, Order, OrderItem, OrderItemBookItem

User = get_user_model()


class BookItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookItem
        fields = ['id', 'rack', 'place', 'book']
        read_only_fields = ['order', ]


class BookSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(many=True, read_only=True, source='bookitem_set')

    class Meta:
        model = Book
        fields = ['id', 'title', 'price', 'book']


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['order', 'book_store', 'quantity']
        read_only_fields = ['order', ]


class OrderSerializer(serializers.ModelSerializer):
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


class OrderItemBookItemSerializer(serializers.ModelSerializer):
    order_item = serializers.HyperlinkedRelatedField(many=True, view_name='orderitem-detail',
                                                     read_only=True)
    book_item = serializers.HyperlinkedRelatedField(many=True, view_name='bookitem-detail',
                                                    read_only=True)

    class Meta:
        model = OrderItemBookItem
        fields = ['id', 'order_item', 'book_item']
