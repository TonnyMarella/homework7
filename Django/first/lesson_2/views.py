from django.http import HttpResponse


def home(request):
    return HttpResponse("<p>This is home!<p>")


def book(request):
    return HttpResponse("This is book!")


def title(request, title):
    return HttpResponse(f'Это глава: "{title}"')


