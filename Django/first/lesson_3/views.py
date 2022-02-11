from django.shortcuts import render
from django.templatetags.static import static
from django.http import HttpResponse, FileResponse
from django.views import View


class MyView(View):
    def get(self, request):
        return HttpResponse("This is Class Based Views")


def main(request):
    return render(request, "hero.html")


def luke(request):
    return HttpResponse("Люк Скайуокер — один из главных персонажей вселенной «Звёздных войн»,"
                        " джедай, сын сенатора с Набу Падме Амидалы Наберри и рыцаря-джедая Энакина Скайуокера.")


def lea(request):
    return HttpResponse("Лея Органа — дочь рыцаря-джедая Энакина Скайуокера и сенатора Падме Амидалы Наберри.")


def xan(request):
    return HttpResponse("Хан. Соло — пилот космического корабля «Тысячелетний сокол», его бортмехаником"
                        " и вторым пилотом является вуки по имени Чубакка. ")


def json(request):
    lets_do_it = [{'priority': 100, 'task': 'Составить список дел'}, {'priority': 150, 'task': 'Изучать Django'},
                  {'priority': 1, 'task': 'Подумать о смысле жизни'}]
    return render(request, "lets_do_it.html", {'lets_do_it': lets_do_it})


def file(request):
    return HttpResponse(open(static('img/002.txt'), "rb"))


def image(request):
    return FileResponse(open(static('001.png'), "rb"))

