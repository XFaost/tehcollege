from django.contrib import admin
from media.models import *
from django.utils.html import format_html

class image_admin(admin.ModelAdmin):
    search_fields = ['image__name', 'description', ]
    list_display = ('image_view', 'create_datetime', )

    def image_view(self, obj):
        return format_html('<img src="{0}" style="max-width:150px;max-height:150px;"/>'.format(obj.image.url))

    image_view.allow_tags = True
    image_view.__name__ = 'Світлина'

admin.site.register(Image, image_admin)