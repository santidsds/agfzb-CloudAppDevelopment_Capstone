from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
def about(request):
    return render(request, 'djangoapp/about.html')

def contact(request):
    return render(request, 'djangoapp/contact.html')

# Create a `login_request` view to handle sign in request
def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect("djangoapp:index")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("djangoapp:index")
    else:
        return redirect("djangoapp:index")


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("djangoapp:index")


# Create a `registration_request` view to handle sign up request
def registration_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
                return redirect('djangoapp:registration')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists.")
                return redirect('djangoapp:registration')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, "Account created successfully.")
                return redirect('djangoapp:index')
        else:
            messages.error(request, "Passwords do not match.")
            return redirect('djangoapp:registration')

    else:
        return render(request, 'djangoapp/registration.html')


# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)
    else:
        return redirect("djangoapp:index")



# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

