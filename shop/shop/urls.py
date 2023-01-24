from django.urls import path

from . import views

urlpatterns = [
    path('book_list', views.BookList.as_view(), name='book_list')

]