from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Book
from .cart import Cart
from .forms import CartAddBookForm
from django.contrib.auth.decorators import login_required


@login_required
@require_POST
def cart_add(request, pk):
    cart = Cart(request)
    book = get_object_or_404(Book, id=pk)
    form = CartAddBookForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(book=book,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart_detail')


@login_required
def cart_remove(request, pk):
    cart = Cart(request)
    book = get_object_or_404(Book, id=pk)
    cart.remove(book)
    return redirect('cart_detail')


@login_required
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
