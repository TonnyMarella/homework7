from django import forms
from django.forms import Textarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Reviews


class UserOurRegistration(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget = Textarea(attrs={'rows': 5})


