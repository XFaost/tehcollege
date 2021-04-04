# Generated by Django 3.1.4 on 2021-04-03 23:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_articlecategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimplePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Назва')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Зміст')),
            ],
            options={
                'verbose_name_plural': 'Статті',
            },
        ),
    ]