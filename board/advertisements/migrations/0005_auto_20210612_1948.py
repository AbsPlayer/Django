# Generated by Django 3.2.4 on 2021-06-12 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0004_auto_20210612_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='other_contact',
            field=models.CharField(blank=True, max_length=100, verbose_name='Прочее'),
        ),
        migrations.AddField(
            model_name='author',
            name='skype',
            field=models.CharField(blank=True, max_length=20, verbose_name='Skype'),
        ),
    ]
