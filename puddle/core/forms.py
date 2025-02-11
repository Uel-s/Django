from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "JohnDoe", "class":"w-full py-2 px-4 rounded-xl"}))    
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "example@gmail.com", "class":"w-full py-2 px-4 rounded-xl"}))    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Enter Password", "class":"w-full py-2 px-4 rounded-xl"}))    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password", "class":"w-full py-2 px-4 rounded-xl"}))    


