from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from .forms import AddPostForm, UploadFileForm
from .models import Women, Category, TagPost

menu = [
    {'title': "О сайте", 'url_name': "about"},
    {'title': "Добавить статью", 'url_name': "add_page"},
    {'title': "Обратная связь", 'url_name': "contact"},
    {'title': "Войти", 'url_name': "login"},
]


def index(request):
    # data_db = Women.published.all()
    data_db = Women.published.all().select_related('cat')
    context = {
        'title': "Главная страница",
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)


def handle_uploaded_file(f):
    with open(f"uploads/{f.name}", "wb") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def about(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            handle_uploaded_file(form.cleaned_data['file'])
    else:
        form = UploadFileForm()
    context = {
        'title': "О сайте",
        'menu': menu,
        'form': form
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
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            # try:
            #     Women.objects.create(**form.cleaned_data)
            #     return redirect('home')
            # except Exception as exc:
            #     print(exc, exc.__class__)
            #     form.add_error(None, f"Ошибка добавления поста: {exc}")

    else:
        form = AddPostForm()
    context = {
        'title': "Добавление статьи",
        'menu': menu,
        'form': form,
    }
    return render(request, 'women/addpage.html', context=context)


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse(f'Авторизация')


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = category.posts.filter(is_published=Women.Status.PUBLISHED)
    context = {
        'title': f"Рубрика: {category.name}",
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }
    return render(request, 'women/index.html', context=context)


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.posts.filter(is_published=Women.Status.PUBLISHED).select_related('cat')
    context = {
        'title': f"Тег: {tag.tag}",
        'menu': menu,
        'posts': posts,
        'cat_selected': None,
    }
    return render(request, 'women/index.html', context=context)
