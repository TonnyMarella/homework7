from django.shortcuts import render, redirect
from .forms import UserOurRegistration
from django.http import HttpResponseRedirect


def registration(request):
    if request.method == 'POST':
        form = UserOurRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return render(request, 'user/register_done.html')
    else:
        form = UserOurRegistration()
    return render(request, 'user/register.html', {'form': form})
