from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from home.models import UserProfile


class RegisterForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'password', 'email', 'first_name', 'last_name']
    # fields = "__all__"


class HomeForm(forms.ModelForm):
    user = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a user...'
        }
    ))

    class Meta:
        model = UserProfile
        fields = ('user',)
        # fields = '__all__'
