from django.urls import include, path

from . import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'order', views.OrderViewSet, basename='order')
router.register(r'orderitem', views.OrderItemViewSet, basename='orderitem')
urlpatterns = [
    path('', include(router.urls)),
]