from datetime import datetime
from .models import GameModel, Gamer
from .forms import CreateUserForm
from .serializers import GameModelSerializer, GamerSerializer

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login

from rest_framework.generics import RetrieveAPIView
from rest_framework import viewsets
from rest_framework.views import Response, APIView

import pytz


class GameViewSet(viewsets.ModelViewSet):
    queryset = GameModel.objects.all().order_by('year')
    serializer_class = GameModelSerializer


class GamerViewSet(viewsets.ModelViewSet):
    queryset = Gamer.objects.all()
    serializer_class = GamerSerializer


class MyRetrieveAPIView(RetrieveAPIView):
    queryset = GameModel.objects.all()
    serializer_class = GameModelSerializer


class MyViewSets(viewsets.ModelViewSet):
    serializer_class = GameModelSerializer
    queryset = GameModel.objects.all()
    lookup_field = 'name'


def index(request):
    return HttpResponse("Privet")


def time(request):
    return render(request, 'time.html')


def time_kiev(request):
    tz = pytz.timezone('Europe/Kiev')
    current_datetime = datetime.now(tz)
    return HttpResponse(current_datetime.time().strftime('%H:%M:%S'))


def time_berlin(request):
    tz = pytz.timezone('Europe/Berlin')
    current_datetime = datetime.now(tz)
    return HttpResponse(current_datetime.time().strftime('%H:%M:%S'))


class PingAPI(APIView):
    def get(self, *args, **kwargs):
        return Response({
            'ping': 'pong'
        })


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(time_kiev)
        else:
            messages.info(request, 'Username or password incorrect')
    context = {}
    return render(request, 'login.html', context)
