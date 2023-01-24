from django.contrib import admin

from .models import Book


@admin.register(Book)
class PostsAdmin(admin.ModelAdmin):
    list_display = ("title", 'price', 'quantity', 'id_in_sklad',)
    fieldsets = [
        (None, {'fields': ['title', 'price', 'quantity', 'id_in_sklad']})]
    list_filter = ['price']
    search_fields = ['title']
    save_as = True
