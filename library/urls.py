from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('register', views.register),
    path('signup', views.signup),
    path('profile', views.profile),
    path('signout', views.signout),
    path('borrowed', views.borrowed),
    path('reserved', views.reserved),
    path('wishlist', views.wishlist),
    path('books', views.books)
]