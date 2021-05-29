from django.contrib import admin
import datetime

from articles.models import *


class tag_admin(admin.ModelAdmin):
    search_fields = ['name', 'description', ]


class article_slider_admin(admin.StackedInline):  # TabularInline StackedInline
    model = ArticleSlider
    extra = 3

    fields = ('slide', 'image_tag',)
    readonly_fields = ('image_tag',)
    autocomplete_fields = ['slide', ]


class article_admin(admin.ModelAdmin):
    search_fields = ['title', ]
    autocomplete_fields = ['create_author', 'tags', ]
    readonly_fields = ('create_author', 'update_author', 'create_datetime', 'update_datetime', 'my_url_link',)
    list_filter = ('tags', 'create_author',)
    exclude = ('url',)
    inlines = [article_slider_admin, ]
    save_on_top = True

    def save_model(self, request, obj, form, change):
        """Після створення статті їй присвоюється автор та час. Якщо оновили статю, присвоюється коли та яка особа
        оновила її """

        if not obj.pk:
            obj.create_author = request.user
            obj.create_datetime = datetime.datetime.now()

        obj.update_author = request.user
        obj.update_datetime = datetime.datetime.now()

        if not obj.pk:
            super().save_model(request, obj, form, change)
            obj.url = "/articles?id=" + str(obj.pk)

        super().save_model(request, obj, form, change)

    def my_url_link(self, instance):
        return format_html('<a href="{url}" target=_blank>{url}</a>', url=instance.url)

    my_url_link.short_description = "Посилання"


class category_admin(admin.ModelAdmin):
    search_fields = ['name', ]
    autocomplete_fields = ['tags', ]
    readonly_fields = ('my_url_link',)
    exclude = ('url',)

    def my_url_link(self, instance):
        return format_html('<a href="{url}" target=_blank>{url}</a>', url=instance.url)

    my_url_link.short_description = "Посилання"

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            super().save_model(request, obj, form, change)
            obj.url = "/articles/category?id=" + str(obj.pk)
        super().save_model(request, obj, form, change)


admin.site.register(Tag, tag_admin)
admin.site.register(Article, article_admin)
admin.site.register(Category, category_admin)
