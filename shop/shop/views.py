from django.shortcuts import render, get_object_or_404
from .models import Book, Order, OrderItem
from .forms import OrderCreateForm
from django.views import generic
from cart.forms import CartAddBookForm
from cart.cart import Cart


class BookList(generic.ListView):
    model = Book
    paginate_by = 5
    template_name = 'shop/book_list.html'
    context_object_name = 'book'


def book_detail(request, pk):
    book = get_object_or_404(Book, id=pk)
    cart_book_form = CartAddBookForm()
    return render(request, 'shop/book_detail.html', {'book': book, 'cart_book_form': cart_book_form})


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user_id = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         book=item['book'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            cart.clear()
            return render(request, 'shop/order_created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'shop/order_create.html', {'cart': cart, 'form': form})
