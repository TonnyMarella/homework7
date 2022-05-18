from django.shortcuts import render, get_object_or_404
from .forms import UserOurRegistration, ProfileForm
from .models import Profile

from datetime import date


def profile(request):
    return render(request, 'user/profile.html')


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


def update_profile(request, user_id):
    profile = get_object_or_404(Profile, user_id=user_id)

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile.birth_date = form.cleaned_data['birth_date']
            if profile.birth_date > date.today():
                return render(request, 'user/update_profile.html', {'error_birth_date': profile.birth_date})
            profile.save()
            return render(request, 'user/profile.html')

    else:
        return render(request, 'user/update_profile.html')

