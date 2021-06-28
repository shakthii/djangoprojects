from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfile

class UserForm(forms.ModelForm):
    #unless you give this one your password field will act as a char field
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ("username","email","password")

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ("portfolio_url","portfolio_pics")
