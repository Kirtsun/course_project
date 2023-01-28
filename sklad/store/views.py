from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Book, BookItem, Order, OrderItem, OrderItemBookItem
from .serializers import OrderSerializer, OrderItemSerializer

User = get_user_model()


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer



