from datetime import datetime

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


def index(request):
    return HttpResponse('Страница приложения Women.')


def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id:{cat_id}<p>')


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug:{cat_slug}<p>')


def archive(request, year):
    current_year = datetime.now().year
    if year > current_year:
        raise Http404()
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}<p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


