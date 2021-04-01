from django.db import models
from django.conf import settings

from ckeditor.fields import RichTextField #https://www.youtube.com/watch?v=mF5jzSXb1dc

class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва')
    description = models.TextField(blank=True, null=True, verbose_name='Опис')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Теги для статей'

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назва')
    content = RichTextField(verbose_name="Зміст")
    create_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='create_author', verbose_name='Автор')
    create_datetime = models.DateTimeField(verbose_name='Створено')    
    update_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='update_author', verbose_name='Автор останнього оновлення')
    update_datetime = models.DateTimeField(verbose_name='Оновлено')
    preview_photo = models.URLField(null=True, blank=True, verbose_name="Прев'ю фото")
    preview_text = models.TextField(verbose_name="Прев'ю тексту")
    tags = models.ManyToManyField(Tag, verbose_name='Теги')    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Статті'

class ArticleCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Назва')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    url = models.URLField(max_length = 4096, blank=True, null=True, verbose_name="Посилання")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категорії статей'