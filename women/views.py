from datetime import datetime

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

menu = [
    {'title': "О сайте", 'url_name': "about"},
    {'title': "Добавить статью", 'url_name': "add_page"},
    {'title': "Обратная связь", 'url_name': "contact"},
    {'title': "Войти", 'url_name': "login"},
]

data_db = [
    {'id': 1, "title": "Анджелина Джоли", "content": "Биография Анджелины Джоли", "is_published": True},
    {'id': 2, "title": "Джессика Симпсон", "content": "Биография Джессики Симпсон", "is_published": False},
    {'id': 34, "title": "Миа Малкова", "content": "Биография Мии Малковой", "is_published": True},
]


def index(request):
    context = {'title': "Главная страница",
               'menu': menu,
               'posts': data_db
               }
    return render(request, 'women/index.html', context=context)


def about(request):
    context = {'title': "О сайте",
               'menu': menu,
               }
    return render(request, 'women/about.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse(f'Авторизация')
