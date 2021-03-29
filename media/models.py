from django.db import models
from django.dispatch import receiver
import os

class Image(models.Model):
    image = models.ImageField(upload_to="images", verbose_name='Світлина')
    description = models.TextField(blank=True, null=True, verbose_name='Опис')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Створено') 

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name_plural = 'Світлини'

@receiver(models.signals.post_delete, sender=Image)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    """
    Видалити світлину з файлової системи
    коли відповідний `Image` об'єкт видаляється
    """
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)

@receiver(models.signals.pre_save, sender=Image)
def auto_delete_image_on_change(sender, instance, **kwargs):
    """
    Видалити стару світлину з файлової системи,
    коли відповідний `Image` об'єкт оновлюється
    з новою світлиною
    """
    if not instance.pk:
        return False

    try:
        old_image = Image.objects.get(pk=instance.pk).image
    except Image.DoesNotExist:
        return False

    new_image = instance.image
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)