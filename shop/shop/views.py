from django.shortcuts import render, get_object_or_404
from .models import Book, Order
from django.views import generic
from cart.forms import CartAddBookForm


class BookList(generic.ListView):
    model = Book
    paginate_by = 5
    template_name = 'shop/book_list.html'
    context_object_name = 'book'


def book_detail(request, pk):
    book = get_object_or_404(Book, id=pk)
    cart_book_form = CartAddBookForm()
    return render(request, 'shop/book_detail.html', {'book': book, 'cart_book_form': cart_book_form})
