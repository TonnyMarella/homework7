from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .models import Article
from django.urls import reverse
from django.contrib.auth.models import User


def index(request):
    article = Article.objects.order_by('-create')
    return render(request, 'article/main.html', {'article': article})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья не найдена...')

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'article/one.html', {'article': a, 'latest_comments_list': latest_comments_list})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404('Статья не найдена...')

    a.comment_set.create(author_name=request.POST['username'], comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('article:detail', args=(a.id,)))


def search(request):
    s = Article.objects.filter(title__icontains=request.GET['search'])
    return render(request, 'article/search.html', {'search_list': s})


def sort_by_alphabet(request):
    article = Article.objects.order_by('title')
    return render(request, 'article/main.html', {'article': article})


def favorite(request):
    user = request.user

    if request.method == 'GET':
        favorite_article = user.article_set.all()
        return render(request, 'article/favorite.html', {'article': favorite_article})

    if request.method == 'POST':
        article = Article.objects.get(id=request.POST['article_id'])
        article.favorite.add(user)
        article.save()
        return HttpResponse(status=204)




