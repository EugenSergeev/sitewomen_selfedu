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
    {'id': 1, "title": "Анджелина Джоли", "content": """<header>
    <h2>Биография Анджелины Джоли</h2>
</header>
<section>
    <h3>Ранние годы</h3>
    <p>
        Анджелина Джоли родилась 4 июня 1975 года в Лос-Анджелесе. Она является дочерью актёров Джона Войта и Марчелин Бертран.
    </p>
</section>
<section>
    <h3>Карьера</h3>
    <p>
        Анджелина начала актёрскую карьеру в раннем возрасте, но настоящую известность получила после роли в фильме "Сквозь дождь" (1998). Она получила "Оскар" за лучшую женскую роль второго плана в фильме "Прерванная жизнь" (1999).
    </p>
</section>
<section>
    <h2>Благотворительная деятельность</h2>
    <p>
        Кроме актёрской карьеры, Анджелина известна своей благотворительной деятельностью. Она является послом доброй воли Верховного комиссара ООН по делам беженцев.
    </p>
</section>
<section>
    <h2>Личная жизнь</h2>
    <p>
        Анджелина была замужем за актёрами Джонни Ли Миллером, Билли Бобом Торнтоном и Брэдом Питтом. У неё есть шесть детей, трое из которых являются приемными.
    </p>
</section>""", "is_published": True},
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
