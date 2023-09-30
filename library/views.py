from datetime import timezone, date, timedelta
import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Book, Borrowed, Reserved, Wishlist
from django.db.models import Q  # Import Q for complex queries
from django.contrib.auth.decorators import login_required









# Welcome:

def welcome(request):
    return render(request, 'library/1welcome.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect(reverse("signup"))
            messages.success(request, "Registration successful!")
        else:
            form = RegistrationForm()
            return render(request, 'library/2register.html', {'form': form, 'message': "Invalid Information"})
    form = RegistrationForm()
    return render(request, 'library/2register.html', {'form': form})

def signup(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("profile"))
        # Otherwise, return login page again with new context
        else:
            return render(request, "library/3signup.html", {
                "message": "Invalid Credentials"
            })
    return render(request, 'library/3signup.html')











# Profile
def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("signup"))
    
    user = request.user
    return render(request, 'library/4profile.html', {'user': user})

def signout(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("welcome"))
    logout(request)
    return render(request, "library/1welcome.html", {
                "message": "Logged Out"
            })



def numOfDays(date1, date2):
  #check which date is greater to avoid days output in -ve number
    if date2 > date1:  
        return (date2-date1).days
    else:
        return (date1-date2).days


def borrowed(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("signup"))
    
    user = request.user
    borrowed_items = Borrowed.objects.filter(user=user)

    for item in borrowed_items:

        day1 = datetime.datetime.now()
        day2 = item.borrow_date
        date1 = date(day1.year, day1.month, day1.day)
        date2 = date(day2.year, day2.month, day2.day)
        item.fine = numOfDays(date1, date2) * 2
        item.return_date = item.borrow_date+timedelta(days=30)

    context = {
        'borrowed_items': borrowed_items
    }
    return render(request, 'library/6borrowed.html', context)


def reserved(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("signup"))
    
    user = request.user  # Get the currently logged-in user
    reserved_items = Reserved.objects.filter(user=user)
    
    context = {
        'reserved_items': reserved_items
    }

    return render(request, 'library/7reserved.html', context)

def wishlist(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("signup"))
    
    user = request.user  # Get the currently logged-in user
    wished_items = Wishlist.objects.filter(user=user)
    
    context = {
        'wished_items': wished_items
    }

    return render(request, 'library/8wishlist.html', context)














#Book
def books(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("signup"))
    
    search_query = request.GET.get('q')

    if search_query:
        books = Book.objects.filter(Q(title__icontains=search_query))
    else:
        books = Book.objects.all()
    return render(request, 'library/9books.html', {'books': books})


def borrow(request, id):

    if request.method == "POST":
        bookx = Book.objects.get(pk=id)
        userx = request.user
        borrowed = Borrowed(book=bookx, user=userx, borrow_date=datetime.datetime.now())
        bookx.num_books_available -= 1
        bookx.save()
        borrowed.save()
    return HttpResponseRedirect(reverse("books"))

def reserve(request, id):

    if request.method == "POST":
        bookx = Book.objects.get(pk=id)
        userx = request.user
        reserved = Reserved(book=bookx, user=userx, borrow_date=datetime.datetime.now())
        reserved.save()
    return HttpResponseRedirect(reverse("books"))

def wish(request, id):

    if request.method == "POST":
        bookx = Book.objects.get(pk=id)
        userx = request.user
        wished = Wishlist(book=bookx, user=userx, borrow_date=datetime.datetime.now())
        wished.save()
    return HttpResponseRedirect(reverse("books"))









# Return
def return_book(request, id):
    item = Borrowed.objects.get(pk = id)
    bookx = Book.objects.get(pk=item.book.id)
    bookx.num_books_available += 1
    bookx.save()
    item.delete()
    return HttpResponseRedirect(reverse("borrowed"))

def remove_reserve(request, id):
    item = Reserved.objects.get(pk = id).delete()
    return HttpResponseRedirect(reverse("reserved"))

def remove_wish(request, id):
    item = Wishlist.objects.get(pk = id).delete()
    return HttpResponseRedirect(reverse("wishlist"))



"""

welcome: Renders the welcome page for the library web application.

register: Handles user registration. If the request method is POST and the registration form is valid, it creates a new user and redirects to the signup page with a success message. Otherwise, it displays the registration form with an error message.

signup: Handles user login. If the request method is POST and the provided credentials are valid, it logs in the user and redirects to the profile page. If the credentials are invalid, it displays the login page with an error message.

profile: Displays the user's profile page. Redirects to the signup page if the user is not authenticated.

signout: Logs out the user and redirects to the welcome page. Redirects to the welcome page with a message if the user is not authenticated.

numOfDays: Helper function for borrowed. Calculates the number of days between two dates

borrowed: Displays the list of books borrowed by the user. Calculates fines for overdue books and displays return dates.

reserved: Displays the list of books reserved by the user.

wishlist: Displays the list of books in the user's wishlist.

books: Displays a list of books. Supports searching for books based on a query parameter.

borrow: Handles the borrowing of a book. Decreases the available count of the book and records the borrowing transaction.

reserve: Handles reserving a book. Records the reservation transaction.

wish: Handles adding a book to the user's wishlist.

return_book: Handles returning a borrowed book. Increases the available count of the book and deletes the borrowing record.

remove_reserve: Handles removing a book from the reserved list.

remove_wish: Handles removing a book from the wishlist.

"""