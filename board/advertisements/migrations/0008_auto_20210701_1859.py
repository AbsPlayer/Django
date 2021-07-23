# Generated by Django 3.2.4 on 2021-07-01 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0007_auto_20210618_1657'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertisement',
            options={'ordering': ['-published_start'], 'verbose_name': 'объявление', 'verbose_name_plural': 'объявления'},
        ),
        migrations.AlterModelOptions(
            name='advertisementstatus',
            options={'verbose_name': 'статус', 'verbose_name_plural': 'статусы'},
        ),
        migrations.AlterModelOptions(
            name='advertisementtype',
            options={'verbose_name': 'тип объявления', 'verbose_name_plural': 'типы объявлений'},
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'автор', 'verbose_name_plural': 'авторы'},
        ),
        migrations.AlterModelOptions(
            name='rubric',
            options={'verbose_name': 'рубрика', 'verbose_name_plural': 'рубрики'},
        ),
    ]
