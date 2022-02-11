from django.http import HttpResponse
from django.template import loader


def lets_do_it(request):
    lets_do = [{'priority': 100, 'task': 'Составить список дел'}, {'priority': 150, 'task': 'Изучать Django'},
                  {'priority': 1, 'task': 'Подумать о смысле жизни'}]
    test_templates = loader.get_template(template_name='lets_do_it.html')
    context = {"lets_do": lets_do}
    print(context)
    return HttpResponse(test_templates.render(context, request))


def heroes(request):
    hero = [{"id": 1, "text": "Люк"},
            {"id": 2, "text": "Лея Органа"},
            {"id": 3, "text": "Хан Соло"}]
    template = loader.get_template(template_name='about_heroes.html')
    context = {"hero": hero}
    return HttpResponse(template.render(context, request))


def about(request, number):
    if number == 1:
        return HttpResponse("Люк Скайуокер — один из главных персонажей вселенной «Звёздных войн»,"
                            " джедай, сын сенатора с Набу Падме Амидалы Наберри и рыцаря-джедая Энакина Скайуокера")
    elif number == 2:
        return HttpResponse("Лея Органа — дочь рыцаря-джедая Энакина Скайуокера и сенатора Падме Амидалы Наберри.")
    elif number == 3:
        return HttpResponse("Хан. Соло — пилот космического корабля «Тысячелетний сокол»,"
                            " его бортмехаником и вторым пилотом является вуки по имени Чубакка. ")


def rulers(request):
    list_rulers = [{'name': 'Шаддам IV', 'surname': 'Коррино'},
                   {'name': 'Пол', 'surname': 'Атрейдес'},
                   {'name': 'Франклин', 'surname': 'Герберт'}]
    template = loader.get_template(template_name='rulers.html')
    context = {"list_rulers": list_rulers}
    return HttpResponse(template.render(context, request))
