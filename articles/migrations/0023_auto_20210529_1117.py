# Generated by Django 3.2 on 2021-05-29 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0022_auto_20210412_1949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articleslider',
            options={'verbose_name_plural': 'Слайдер'},
        ),
        migrations.RenameField(
            model_name='articleslider',
            old_name='image',
            new_name='slide',
        ),
    ]
