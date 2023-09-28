from django.shortcuts import render
from django.http import HttpResponse
from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    student_id = forms.IntegerField(label='Std ID')
    email = forms.EmailField(label='Email')

class SignUpForm(forms.Form):
    student_id = forms.IntegerField(label='Std ID')
    email = forms.EmailField(label='Email')

# Create your views here.

def welcome(request):
    return render(request, 'library/1welcome.html')

def register(request):
    if request.method == "POST":
        form = RegistrationForm()

        if form.is_valid():
            pass

        else:
            pass

    return render(request, 'library/2register.html', 
    {'form': RegistrationForm()} )

def signup(request):
    return render(request, 'library/3signup.html',
    {'form': SignUpForm()})

def profile(request):
    return render(request, 'library/4profile.html')

def signout(request):
     return HttpResponse('Signout')

def borrowed(request):
    return render(request, 'library/6borrowed.html')

def reserved(request):
    return render(request, 'library/7reserved.html')

def wishlist(request):
    return render(request, 'library/8wishlist.html')

def books(request):
    return render(request, 'library/9books.html')
