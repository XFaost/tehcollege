from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

"""Шлях до файлу, який містить елементи навігації. Він зменшує навантаження на БД"""
NAVIGATION_JSON_PATH = 'navigation/saved_navigation.json'

class Navigation(MPTTModel):
    #https://stackoverflow.com/questions/60120266/django-categories-and-subcategories
    name = models.CharField(max_length=256, verbose_name="Ім'я")
    url = models.URLField(max_length=4096, verbose_name="Посилання")    
    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='child',
        verbose_name="Підкатегорія",
        on_delete=models.CASCADE
    )

    def __str__(self):                           
        return self.name

    class Meta:
        verbose_name_plural = "Елементи навігації"



        