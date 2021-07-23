from django.contrib import admin, messages
from django.conf import settings
from advertisements.models import Advertisement, Rubric, Author, AdvertisementStatus, AdvertisementType
from django.core.exceptions import ObjectDoesNotExist


class AdvertisementInLine(admin.TabularInline):
    model = Advertisement


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'photo', 'author', 'created', 'status', 'type', 'rubric']
    list_filter = ['status', 'type', 'rubric']
    search_fields = ['title', 'description']

    actions = [
        'mark_as_active',
        'mark_as_archive',
        'mark_as_draft'
    ]

    try:
        status_id_active = AdvertisementStatus.objects.get(name=settings.ADVERTISEMENT_STATUS_ACTIVE).id
    except ObjectDoesNotExist:
        status_id_active = None
    try:
        status_id_draft = AdvertisementStatus.objects.get(name=settings.ADVERTISEMENT_STATUS_DRAFT).id
    except ObjectDoesNotExist:
        status_id_draft = None
    try:
        status_id_archive = AdvertisementStatus.objects.get(name=settings.ADVERTISEMENT_STATUS_ARCHIVE).id
    except ObjectDoesNotExist:
        status_id_archive = None

    def mark_as_active(self, request, queryset):
        if self.status_id_active:
            queryset.update(status=self.status_id_active)
        else:
            self.message_user(request, message='Такого статуса не существует в БД', level=messages.WARNING)

    def mark_as_archive(self, request, queryset):
        if self.status_id_archive:
            queryset.update(status=self.status_id_archive)
        else:
            self.message_user(request, message='Такого статуса не существует в БД', level=messages.WARNING)

    def mark_as_draft(self, request, queryset):
        if self.status_id_draft:
            queryset.update(status=self.status_id_draft)
        else:
            self.message_user(request, message='Такого статуса не существует в БД', level=messages.WARNING)

    mark_as_active.short_description = f'Перевести в статус {settings.ADVERTISEMENT_STATUS_ACTIVE}'
    mark_as_draft.short_description = f'Перевести в статус {settings.ADVERTISEMENT_STATUS_DRAFT}'
    mark_as_archive.short_description = f'Перевести в статус {settings.ADVERTISEMENT_STATUS_ARCHIVE}'


@admin.register(Rubric)
class RubricAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'email', 'phone_number']
    list_filter = ['user', 'first_name', 'last_name', 'phone_number']
    search_fields = ['user', 'first_name', 'last_name']
    inlines = [AdvertisementInLine]
    fieldsets = (
        ('Основные сведения', {
            'fields': ('user', 'first_name', 'last_name', 'phone_number')
        }),
        ('Контактные данные', {
            'fields': ('email', 'web', 'facebook', 'viber', 'telegram', 'whatsapp', 'skype', 'other_contact'),
            'description': 'личный сайт, facebook, мессенджеры',
            'classes': ['collapse']
        })
    )


@admin.register(AdvertisementStatus)
class AdvertisementStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertisementType)
class AdvertisementTypeAdmin(admin.ModelAdmin):
    pass
