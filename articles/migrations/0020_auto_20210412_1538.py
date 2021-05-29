# Generated by Django 3.2 on 2021-04-12 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_auto_20210404_2209'),
        ('articles', '0019_auto_20210406_0404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='preview_photo',
        ),
        migrations.AddField(
            model_name='article',
            name='slider',
            field=models.ManyToManyField(blank=True, to='media.Image', verbose_name='Слайдер'),
        ),
    ]