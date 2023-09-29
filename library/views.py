from datetime import timezone
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Book, Borrowed  # Import your Book model
from django.db.models import Q  # Import Q for complex queries

# Create your views here.

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
        messages.error(request, "Registration failed. Please correct the errors.")  # Error message
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

def borrowed(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("signup"))
    

    if request.method == "POST":
        book = Book.objects.get()
        borrow_date = timezone.now()  # You can use any method to get the current date
        borrowed_book = Borrowed(book=book, user=request.user, borrow_date=borrow_date)
        borrowed_book.save()
        book.availability_status -= 1
        book.save()
        return HttpResponseRedirect(reverse("books"))

    return render(request, 'library/6borrowed.html')

def reserved(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("signup"))
    return render(request, 'library/7reserved.html')

def wishlist(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("signup"))
    return render(request, 'library/8wishlist.html')

def books(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("signup"))
    
    search_query = request.GET.get('q')

    if search_query:
        books = Book.objects.filter(Q(title__icontains=search_query))
    else:
        books = Book.objects.all()
    return render(request, 'library/9books.html', {'books': books})




