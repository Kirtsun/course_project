from django.contrib import admin

from .models import Book, Order, OrderItem


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", 'price', 'quantity', 'id_in_sklad',)
    fieldsets = [
        (None, {'fields': ['title', 'price', 'quantity', 'id_in_sklad']})]
    list_filter = ['price']
    search_fields = ['title']
    save_as = True


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['book']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'status', 'city',
                    'address']
    list_filter = ['status']
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'book', 'price', 'quantity']
