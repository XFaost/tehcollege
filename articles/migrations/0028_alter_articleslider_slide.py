# Generated by Django 3.2.3 on 2021-05-29 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_auto_20210404_2209'),
        ('articles', '0027_alter_articleslider_slide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleslider',
            name='slide',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.image', verbose_name='Слайд'),
        ),
    ]
