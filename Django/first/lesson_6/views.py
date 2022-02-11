from django.views.generic import ListView
from .models import GameModel
from django.http import HttpResponse


class FilterView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name__startswith='L')


class FilerNumView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name__regex=r'[\d]').order_by('year')


class ExcludeView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.exclude(name='Left 4 Dead')


class OrderBy(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.exclude(name='Left 4 Dead').order_by('year')


class Union(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.exclude(name='Left 4 Dead').order_by('year').union(
        GameModel.objects.filter(name='Left 4 Dead')
    )


class AllView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.all()


class Values(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name='Left 4 Dead').values('year')


def get_view(request):
    date = GameModel.objects.get(pk=2)
    print(date)
    return HttpResponse(date)

