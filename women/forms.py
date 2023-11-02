from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, BaseValidator
from django.utils.deconstruct import deconstructible

from .models import Category, Husband


@deconstructible
class RussianValidator:
    ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщэюя0123456789- "
    code = 'russian'

    def __init__(self, message=None):
        self.message = message if message else "Должны присутствовать только русские символы, дефис и пробел"

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=5, help_text="Название статьи",
                            label="Заголовок", widget=forms.TextInput(attrs={'class': 'form-input'}),
                            validators=[RussianValidator(),],
                            error_messages={
                                "min_length": "Слишком короткий заголовок",
                                'required': "Без заголовка никак нельзя"
                            })
    # widget=forms.TextInput(attrs={'class': 'form-input'}) - позволяет назначить кастомный класс

    # slug = forms.SlugField(max_length=255, validators=[
    #     MinLengthValidator(5, message="Минимум 5 символов"),
    #     MaxLengthValidator(100, message="Максимум 100 символов")
    # ])
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), help_text="Текст статьи",
                              required=False, label="Контент")
    is_published = forms.BooleanField(required=False, label="Для публикации", initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категории", empty_label="Выбери категорию")
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), required=False, label="Муж",
                                     empty_label="Не замужем")
