# Generated by Django 3.1.4 on 2021-03-29 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20210329_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='preview_text',
            field=models.TextField(verbose_name="Прев'ю тексту"),
        ),
    ]
