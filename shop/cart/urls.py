from django.urls import path
from . import views


urlpatterns = [
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('add/<int:pk>', views.cart_add, name='cart_add'),
    path('remove/<int:pk>', views.cart_remove, name='cart_remove')
]
