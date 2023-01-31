from django.contrib import admin

from .models import Book, BookItem, Order, OrderItem


class BookInLineBookItem(admin.TabularInline):
    model = BookItem
    extra = 3


class OrderItemInLineOrder(admin.TabularInline):
    model = OrderItem
    extra = 3


class OrderItemInLineBook(admin.TabularInline):
    model = OrderItem
    extra = 3


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']
    list_display_links = ['title', 'price']
    inlines = [BookInLineBookItem, OrderItemInLineBook]


@admin.register(BookItem)
class BookItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'place', 'book', 'rack']
    list_display_links = ['place']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'user_email', 'status', 'city', 'address', 'order_id_in_shop']
    list_display_links = ['user', 'id']
    inlines = [OrderItemInLineOrder]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'book_store', 'quantity']
    list_display_links = ['id', 'order']



