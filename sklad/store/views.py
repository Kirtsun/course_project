
from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Book, BookItem, Order, OrderItem, OrderItemBookItem
from .serializers import BookSerializer, BookItemSerializer, OrderSerializer, OrderItemSerializer,\
    OrderItemBookItemSerializer

User = get_user_model()


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookItemViewSet(viewsets.ModelViewSet):
    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderItemBookItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItemBookItem.objects.all()
    serializer_class = OrderItemBookItemSerializer
