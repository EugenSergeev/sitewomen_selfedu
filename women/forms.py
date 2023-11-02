from django import forms
from .models import Category, Husband


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label="Заголовок", widget=forms.TextInput(attrs={'class': 'form-input'}))
    # widget=forms.TextInput(attrs={'class': 'form-input'}) - позволяет назначить кастомный класс

    # slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), required=False, label="Контент")
    is_published = forms.BooleanField(required=False, label="Для публикации", initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категории", empty_label="Выбери категорию")
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, label="Муж",
                                     empty_label="Не замужем")
