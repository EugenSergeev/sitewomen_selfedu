from django.contrib import admin, messages

from women.models import Women, Category, TagPost, Husband


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'is_published', 'cat', 'husband', 'brief_info')
    list_display_links = ('title',)
    ordering = ['-time_create', 'title']
    list_editable = ('is_published', 'cat', 'husband')
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    search_fields = ('title', 'cat__name')

    @admin.display(description="Длина статьи", ordering='content')
    def brief_info(self, women: Women):
        return len(women.content)

    @admin.action(description="Опубликовать")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей")

    @admin.action(description="Снять с публикации")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f"{count} записей сняты с публикации.", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'brief_info']
    list_display_links = ['name']

    @admin.display(description="Количество записей")
    def brief_info(self, cat: Category):
        return cat.posts.count()


@admin.register(TagPost)
class TagPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag', 'brief_info']
    list_display_links = ['tag']

    @admin.display(description="Количество записей")
    def brief_info(self, tag: TagPost):
        return tag.posts.count()


@admin.register(Husband)
class HusbandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']
    list_display_links = ['name']
