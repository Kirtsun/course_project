from django.urls import include, path

from . import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'book', views.BookViewSet, basename="book")
router.register(r'book_item', views.BookItemViewSet, basename='book_item')
router.register(r'order', views.OrderViewSet, basename='order')
router.register(r'order_item', views.OrderItemViewSet, basename='order_item')
router.register(r'order_item_book_item', views.OrderItemBookItemViewSet, basename='order_item_book_item')
urlpatterns = [
    path('', include(router.urls)),
]