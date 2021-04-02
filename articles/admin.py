from django.contrib import admin
from articles.models import *
from django.utils.html import format_html

import datetime


class tag_admin(admin.ModelAdmin):
    search_fields = ['name', 'description', ]


class article_admin(admin.ModelAdmin):
    search_fields = ['title', ]
    autocomplete_fields = ['create_author', 'tags', ]
    readonly_fields = ('create_author', 'update_author', 'create_datetime', 'update_datetime',)
    list_filter = ('tags', 'create_author',)

    def save_model(self, request, obj, form, change):
        """Після створення статті їй присвоюється автор та час. Якщо оновили статю, присвоюється коли та яка особа
        оновила її """
        if not obj.pk:
            obj.create_author = request.user
            obj.create_datetime = datetime.datetime.now()
        obj.update_author = request.user
        obj.update_datetime = datetime.datetime.now()
        super().save_model(request, obj, form, change)


class article_category_admin(admin.ModelAdmin):
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
admin.site.register(ArticleCategory, article_category_admin)
