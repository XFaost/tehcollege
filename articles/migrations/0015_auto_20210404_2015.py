# Generated by Django 3.1.4 on 2021-04-04 17:15

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_auto_20210404_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Зміст'),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Зміст'),
        ),
    ]
