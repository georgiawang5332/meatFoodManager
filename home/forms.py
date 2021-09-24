from django import forms
from home.models import UserProfile


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
