from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User

# accounts/forms.py
from django import forms
from django.contrib.auth.models import User

class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100, required=True)  # Editable
    last_name = forms.CharField(max_length=100, required=True)   # Editable
    email = forms.EmailField(required=True)  # Editable

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']  # Corrected fields

