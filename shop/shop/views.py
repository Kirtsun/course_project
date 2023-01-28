from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import Book, OrderItem
from .forms import OrderCreateForm
from cart.forms import CartAddBookForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from .filter import BookFilter
from django.core.mail import send_mail
from .tasks import send_order, sync_book


def book_list(request):
    qset = Book.objects.all()
    f = BookFilter(request.GET, queryset=qset)
    qs = f.qs
    paginator = Paginator(qs, 4)
    page = request.GET.get('page', 1)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'shop/book_list.html', {'filter': f, 'paginator': paginator, 'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, id=pk)
    cart_book_form = CartAddBookForm()
    return render(request, 'shop/book_detail.html', {'book': book, 'cart_book_form': cart_book_form})


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.status = 'ORDERED'
            order.save()
            send_mail('Order in a bookstore.', f'Your order number {order.id}. When it is executed you will receive'
                                               f' a notification!', 'bookstore@example.com', [order.user.email],
                      fail_silently=False,)
            for item in cart:
                OrderItem.objects.create(order=order,
                                         book=item['book'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            cart.clear()
            send_order.delay(order_id=order.id)
            return render(request, 'shop/order_created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'shop/order_create.html', {'cart': cart, 'form': form})
