from django.urls import path

from . import views

urlpatterns = [
    path('book_list/', views.book_list, name='book_list'),
    path('book_detail/<int:pk>', views.book_detail, name='book_detail'),
    path('order_create/', views.order_create, name='order_create')
]
