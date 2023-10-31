from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from transliterate import slugify as transliterate_slugify


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


class Women(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, "Черновик"
        PUBLISHED = 1, "Опубликовано"

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return f'<Women: {self.title}>'

    def save(self, *args, **kwargs):
        self.slug = transliterate_slugify(self.title) or slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
