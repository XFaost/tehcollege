from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from navigation.services import *


class navigation_admin(DraggableMPTTAdmin):
    search_fields = ['name', 'url', ]
    autocomplete_fields = ['parent', ]

    def save_model(self, request, obj, form, change):
        """Після кожного оновлення навігації оновлюємо й файл, який зберігає у собі його елементи"""
        super().save_model(request, obj, form, change)
        navigation_to_json_file()


admin.site.register(Navigation, navigation_admin)
