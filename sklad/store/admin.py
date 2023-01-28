from django.contrib import admin

from .models import Book, BookItem, Order, OrderItem, OrderItemBookItem


class BookInLineBookItem(admin.TabularInline):
    model = BookItem
    extra = 3


class BookItemInLineOrderItemBookItem(admin.TabularInline):
    model = OrderItemBookItem.book_item.through
    extra = 3


class OrderItemInLineOrderItemBookItem(admin.TabularInline):
    model = OrderItemBookItem.order_item.through
    extra = 3


class OrderItemInLineOrder(admin.TabularInline):
    model = OrderItem
    extra = 3


class OrderItemInLineBook(admin.TabularInline):
    model = OrderItem
    extra = 3


class OrderItemBookItemInLineOrderItem(admin.TabularInline):
    model = OrderItemBookItem.order_item.through
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
    inlines = [BookItemInLineOrderItemBookItem]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'user_email', 'status', 'city', 'address', 'order_id_in_shop']
    list_display_links = ['user', 'id']
    inlines = [OrderItemInLineOrder]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'book_store', 'quantity']
    list_display_links = ['id', 'order']
    inlines = [OrderItemBookItemInLineOrderItem]


@admin.register(OrderItemBookItem)
class OrderItemBookItemAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']

