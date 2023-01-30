
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import Book, BookItem, Order, OrderItem, OrderItemBookItem
from .serializers import BookSerializer, BookItemSerializer, OrderSerializer, OrderItemSerializer,\
    OrderItemBookItemSerializer

import django_filters

User = get_user_model()


class OrderFilter(django_filters.FilterSet):

    class Meta:
        model = Order
        fields = {
            'order_id_in_shop': ['in']
        }


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookItemViewSet(viewsets.ModelViewSet):
    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = OrderFilter


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderItemBookItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItemBookItem.objects.all()
    serializer_class = OrderItemBookItemSerializer
