from django.contrib import admin, messages

from women.models import Women, Category, TagPost, Husband


class MarriedFilter(admin.SimpleListFilter): # кастомный фильтр
    title = "Стутас женщин" # name of filter
    # параметр, который будет передаваться в адресной строке со значением определённым в lookups
    parameter_name = "status"

    def lookups(self, request, model_admin):
        # возможные значения параметров
        return [
            ("married", "Замужем"),
            ("single", "Не замужем")
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        else:
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    # поля, которые можно будет изменять при редактировании записи или создании новой записи
    fields = ('title', 'slug', 'content', 'cat', 'tags', 'husband')
    # exclude = ('slug', ) # поля, которые нужно исключить из редактирования
    readonly_fields = ('slug', ) # обозначение полей только для просмотра
    # prepopulated_fields = {'slug': ("title",)} # Автозаполнение поля slug из поля title
    filter_horizontal = ('tags', )  # улучшает вид выбора для связи многие ко многим
    list_display = ('title', 'time_create', 'is_published', 'cat', 'husband', 'brief_info')
    list_display_links = ('title',) # Какие столбцы являются ссылками на редактирование записи
    ordering = ['-time_create', 'title'] # Сортировка по полям
    list_editable = ('is_published', 'cat', 'husband') # Редактируемые поля. Нельзя редактировать поля типа ManyToMany
    list_per_page = 5 # Пагинация
    # Добавляет новые действия с записями. Действия должны быть прописаны в классе.
    actions = ['set_published', 'set_draft']
    # Добавляет панель поиска. cat__name - позволяет вести поиск по конкретному полю зависимого класса
    search_fields = ('title', 'cat__name')
    list_filter = (MarriedFilter, 'cat__name', 'is_published') # Добавляет панель фильтрации

    @admin.display(description="Длина статьи", ordering='content')
    def brief_info(self, women: Women): # Добавляет новый столбец
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
