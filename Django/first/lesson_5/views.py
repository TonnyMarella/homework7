from django.shortcuts import render
from django.http import HttpResponse
from . import forms


def simple_form(request):
    return HttpResponse(forms.MyForms().as_p())


def my_form(request):
    form = forms.FromFromModel(request.GET)
    return render(request, 'form_page.html', context={'form': form})


def my_modelform(request):
    form = forms.MyModelForm(request.GET)
    return render(request, 'form_page.html', context={'form': form})


