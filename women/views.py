from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from .models import Women

menu = [
    {'title': "О сайте", 'url_name': "about"},
    {'title': "Добавить статью", 'url_name': "add_page"},
    {'title': "Обратная связь", 'url_name': "contact"},
    {'title': "Войти", 'url_name': "login"},
]

cats_db = [
    {'id': 1, 'name': "Актрисы"},
    {'id': 2, 'name': "Певицы"},
    {'id': 3, 'name': "Спортсменки"},
]


def index(request):
    data_db = Women.objects.filter(is_published=1)
    data_db = Women.published.all()

    context = {
        'title': "Главная страница",
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    context = {'title': "О сайте",
               'menu': menu,
               }
    return render(request, 'women/about.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    context = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1
    }
    return render(request, 'women/post.html', context=context)


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse(f'Авторизация')


def show_category(request, cat_id):
    data_db = Women.objects.all()
    context = {
        'title': "Отображение по рубрикам",
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)
