from django.shortcuts import render
from .models import Book, Order
from django.views import generic


class BookList(generic.ListView):
    model = Book
    paginate_by = 5
    template_name = 'shop/book_list.html'
    context_object_name = 'book'
