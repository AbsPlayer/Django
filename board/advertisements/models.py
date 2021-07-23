from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Advertisement(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name=_('объявление'))
    description = models.TextField(null=True, blank=True, db_index=True, verbose_name=_('описание'))
    price = models.FloatField(default=0, null=True, blank=True, verbose_name=_('цена'))
    created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=_('создано'))
    published_start = models.DateTimeField(auto_now=True, db_index=True, verbose_name=_('опубликовано'))
    photo = models.ImageField(default=None, upload_to='files/')
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisements', verbose_name=_('статус'))
    type = models.ForeignKey('AdvertisementType', default=None, null=True, on_delete=models.CASCADE,
                             related_name='advertisements', verbose_name=_('тип объявления'))
    author = models.ForeignKey('Author', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisements', verbose_name=_('автор'))
    rubric = models.ForeignKey('Rubric', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisements', verbose_name=_('рубрика'))

    class Meta:
        verbose_name_plural = _('объявления')
        verbose_name = _('объявление')
        ordering = ['-published_start']

    def __str__(self):
        return self.title


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('статус'))

    class Meta:
        verbose_name_plural = _('статусы')
        verbose_name = _('статус')

    def __str__(self):
        return self.name


class AdvertisementType(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('тип объявления'))

    class Meta:
        verbose_name_plural = _('типы объявлений')
        verbose_name = _('тип объявления')

    def __str__(self):
        return self.name


class Author(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, db_index=True, blank=True, verbose_name=_('имя'))
    last_name = models.CharField(max_length=50, db_index=True, blank=True, verbose_name=_('фамилия'))
    email = models.EmailField(verbose_name='EMail')
    phone_number = models.CharField(max_length=12, null=True, db_index=True, verbose_name=_('номер телефона'))
    web = models.URLField(blank=True, verbose_name=_('веб-страница'))
    facebook = models.URLField(blank=True, verbose_name='facebook')
    viber = models.CharField(max_length=20, blank=True, verbose_name='Viber')
    telegram = models.CharField(max_length=20, blank=True, verbose_name='Telegram')
    whatsapp = models.CharField(max_length=20, blank=True, verbose_name='WhatsApp')
    skype = models.CharField(max_length=20, blank=True, verbose_name='Skype')
    other_contact = models.CharField(max_length=100, blank=True, verbose_name=_('Прочее'))

    class Meta:
        verbose_name_plural = _('авторы')
        verbose_name = _('автор')

    def __str__(self):
        return self.user.username


class Rubric(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name=_('рубрика'))

    class Meta:
        verbose_name_plural = _('рубрики')
        verbose_name = _('рубрика')

    def __str__(self):
        return self.name
