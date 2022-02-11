from django.shortcuts import render
from django.http import HttpResponse
from .models import GameModel, Gamer


def security_test(request):
    print(request.POST.get('user_input'))
    print(request.POST.get('user_input_sql'))
    try:
        result_sql = GameModel.objects.raw(request.POST.get('user_input_sql'))
        result = [result for result in reuslt_sql]
    except Exception as e:
        print(e)
        result = []

    return render(request, 'security_test.html',
                  context={'my_variable': request.POST.get('user_input')})


def ajax_check(request):
    return HttpResponse('success')
