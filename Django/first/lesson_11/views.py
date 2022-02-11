from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    return HttpResponse("<p>Hello World!<p>")


def lesson_11(request):
    return HttpResponse("<p>Hello World!</p><p>Django is one of the best framework on Python</p><hr>")


def bio(request, username):
    return HttpResponse(f'Пользователь с именем: "{username}"')