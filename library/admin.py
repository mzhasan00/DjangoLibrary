from django.contrib import admin
from .models import Book, Borrowed, Reserved, Wishlist

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'ISBN', 'publication_date', 'genre', 'availability_status', 'num_books_available')

class BorrowedAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'borrow_date')

class ReservedAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'borrow_date')

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'borrow_date')

admin.site.register(Book, BookAdmin)
admin.site.register(Borrowed, BorrowedAdmin)
admin.site.register(Reserved, ReservedAdmin)
admin.site.register(Wishlist, WishlistAdmin)

