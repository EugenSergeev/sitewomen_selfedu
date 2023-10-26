from datetime import datetime

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    context = {'title': "Главная страница",
               'menu': menu,
               'float': 2.1,
               'list': [1, 2, 3],
               }
    return render(request, 'women/index.html', context=context)

def about(request):
    return render(request, 'women/about.html', context={'title': "About site"})

def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id:{cat_id}<p>')


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug:{cat_slug}<p>')


def archive(request, year):
    current_year = datetime.now().year
    if year > current_year:
        uri = reverse('cats', args=('music',))
        return HttpResponseRedirect(uri)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}<p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


