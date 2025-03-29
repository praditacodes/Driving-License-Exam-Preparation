from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import QuesModel, Profile
from accounts.forms import ProfileUpdateForm  
# Add ProfileUpdateForm here
from django import forms
from django.contrib.auth.models import User
from django import forms
from .models import QuesModel


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']  # Include the profile picture field from the Profile model

class createuserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']  # Include both password fields for user creation

class addQuestionform(forms.ModelForm):
    class Meta:
        model = QuesModel
        fields = "__all__"  # Include all fields of the QuesModel for the form



class QuizProfileUpdateForm(forms.ModelForm):  # Renamed the form to avoid conflict
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
  # Include fields you want to allow users to update




class QuesModelForm(forms.ModelForm):
    class Meta:
        model = QuesModel
        fields = ['question', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_answer']
