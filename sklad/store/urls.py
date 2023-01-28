from django.urls import include, path

from . import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'book', views.BookViewSet, basename="book")
router.register(r'bookitem', views.BookItemViewSet, basename='bookitem')
router.register(r'order', views.OrderViewSet, basename='order')
router.register(r'orderitem', views.OrderItemViewSet, basename='orderitem')
router.register(r'orderitembookitem', views.OrderItemBookItemViewSet, basename='orderitembookitem')
urlpatterns = [
    path('', include(router.urls)),
]
