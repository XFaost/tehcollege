from django.db import models
from django.conf import settings

from ckeditor_uploader.fields import RichTextUploadingField  # https://www.youtube.com/watch?v=L6y6cn1XUfw
from django.utils.html import format_html

from media.models import Image


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва')
    description = models.TextField(blank=True, null=True, verbose_name='Опис')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Теги'
        db_table = 'tags'


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назва')

    preview_text = models.TextField(verbose_name='Прев\'ю тексту')

    content = RichTextUploadingField(verbose_name='Зміст')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    is_hide = models.BooleanField(default=False, verbose_name='Сховати')

    create_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='create_author', verbose_name='Автор')
    create_datetime = models.DateTimeField(verbose_name='Створено')
    update_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, related_name='update_author', verbose_name='Автор останнього оновлення')
    update_datetime = models.DateTimeField(verbose_name='Оновлено')
    url = models.URLField(max_length=4096, blank=True, null=True, verbose_name='Посилання')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Статті'
        db_table = 'article'


class ArticleSlider(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Стаття')
    slide = models.ForeignKey(Image, on_delete=models.CASCADE, verbose_name='Слайд')

    def image_tag(self):
        return format_html('<img src="{0}" style="max-width:150px;max-height:150px;"/>'.format(self.slide.image.url))
    image_tag.short_description = 'Прев\'ю'
    image_tag.allow_tags = True

    def __str__(self):
        return str(self.article.id) + ' - ' + self.slide.image.name

    class Meta:
        verbose_name_plural = 'Слайдер'
        db_table = 'article_slider'


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Назва')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    url = models.URLField(max_length=4096, blank=True, null=True, verbose_name='Посилання')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категорії'
        db_table = 'category'
