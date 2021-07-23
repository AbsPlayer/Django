# Generated by Django 3.2.4 on 2021-06-11 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisementStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='статус')),
            ],
        ),
        migrations.CreateModel(
            name='AdvertisementType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='тип объявления')),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='имя')),
                ('email', models.EmailField(max_length=254, verbose_name='EMail')),
                ('phone_number', models.CharField(db_index=True, max_length=12, null=True, verbose_name='номер телефона')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='рубрика')),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрики',
            },
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, verbose_name='объявление')),
                ('description', models.TextField(blank=True, db_index=True, null=True, verbose_name='описание')),
                ('price', models.FloatField(blank=True, default=0, null=True, verbose_name='цена')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='создано')),
                ('published_start', models.DateTimeField(auto_now=True, db_index=True, verbose_name='опубликовано')),
                ('published_end', models.DateTimeField(db_index=True, null=True, verbose_name='окончание публикации')),
                ('views_count', models.IntegerField(default=0, verbose_name='количество просмотров')),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='advertisements.author', verbose_name='автор')),
                ('rubric', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='advertisements.rubric', verbose_name='рубрика')),
                ('status', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='advertisements.advertisementstatus', verbose_name='статус')),
                ('type', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='advertisements.advertisementtype', verbose_name='тип объявления')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': ['-published_start'],
            },
        ),
    ]
