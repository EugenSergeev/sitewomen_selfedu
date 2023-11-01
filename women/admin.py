from django.contrib import admin

from women.models import Women, Category, TagPost, Husband


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'time_create', 'is_published', 'cat', 'husband']
    list_display_links = ['id', 'title']
    ordering = ['-time_create', 'title']
    list_editable = ('is_published', 'cat', 'husband')
    list_per_page = 5


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']


@admin.register(TagPost)
class TagPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag']
    list_display_links = ['tag']


@admin.register(Husband)
class HusbandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']
    list_display_links = ['name']
