from django.db import models
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import SignUpForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from django.shortcuts import render
from .forms import ProfileUpdateForm

def profile(request):
    user = request.user
    form = ProfileUpdateForm(instance=user)  # Instantiate the form with the user's data
    return render(request, 'profile.html', {'form': form})


# Create your models here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# @login_required
# def profile(request):
#     return render(request, 'profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page after update
    else:
        form = ProfileUpdateForm(instance=request.user)
    
    return render(request, 'profile_update.html', {'form': form})


