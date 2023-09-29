from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('register', views.register, name='register'),
    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('signout', views.signout, name='signout'),
    path('borrowed', views.borrowed, name='borrowed'),
    path('reserved', views.reserved, name='reserved'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('books', views.books, name='books'),
    path("borrow/<int:id>", views.borrow, name="borrow"),
    path("reserv/<int:id>", views.reserve, name="reserve"),
    path("wish/<int:id>", views.wish, name="wish"),
    path("return_book/<int:id>", views.return_book, name="return_book"),
    path("remove_reserve/<int:id>", views.remove_reserve, name="remove_reserve")


]