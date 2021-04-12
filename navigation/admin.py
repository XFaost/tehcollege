from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from navigation.services import *


class navigation_admin(DraggableMPTTAdmin):
    search_fields = ['name', 'url', ]
    autocomplete_fields = ['parent', ]
    actions = ['delete_queryset']

    def save_model(self, request, obj, form, change):
        """Після кожного оновлення навігації оновлюємо й файл, який зберігає у собі його елементи"""
        super().save_model(request, obj, form, change)
        navigation_to_json_file()

    def delete_model(self, request, obj):
        """Після кожного видалення елемента навігації оновлюємо й файл, який зберігає у собі усі елементи навігації"""
        obj.delete()
        navigation_to_json_file()

    def get_actions(self, request):
        """Прибираємо delete_selected, адже її не можна переоприділити. Створюємо свою функцію для видалення виділених обєктів: delete_queryset"""
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def delete_queryset(self, request, queryset):
        """Після кожного видалення виділених елементів навігації оновлюємо й файл, який зберігає у собі усі елементи навігації"""
        queryset.delete()
        navigation_to_json_file()

    delete_queryset.short_description = "Видалити вибрані Елементи навігації та оновити меню на сайті"


admin.site.register(Navigation, navigation_admin)
