from django import forms
from .models import Client, Car


class MyForms(forms.Form):
    image = forms.ImageField(label="Фотография машины")
    email = forms.EmailField()
    descriptions = forms.CharField()
    evaluation = forms.IntegerField()
    review = forms.BooleanField(required=False)
    phone_number = forms.CharField(max_length=13)


class FromFromModel(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['email', 'name']


class MyModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'price']
