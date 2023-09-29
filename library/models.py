from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    genre = models.CharField(max_length=100)
    availability_status = models.BooleanField(default=True)
    num_books_available = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title


class Borrowed(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title} on {self.borrow_date}"
    

class Reserved(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title} on {self.borrow_date}"
    

class Wishlist(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title} on {self.borrow_date}"