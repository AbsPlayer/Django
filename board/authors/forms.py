from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from advertisements.models import Author


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'web',
            'facebook',
            'viber',
            'telegram',
            'whatsapp',
            'skype',
            'other_contact'
        ]


class ExtendedRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=12, required=True)
    web = forms.URLField(required=False, help_text='личный сайт (необязательно)')
    facebook = forms.URLField(required=False, help_text='(необязательно)')
    viber = forms.CharField(required=False, help_text='(необязательно)')
    telegram = forms.CharField(required=False, help_text='(необязательно)')
    whatsapp = forms.CharField(required=False, help_text='(необязательно)')
    skype = forms.CharField(required=False, help_text='(необязательно)')
    other_contact = forms.CharField(max_length=100, required=False, help_text='другие контакты (необязательно)')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'web',
            'facebook',
            'viber',
            'telegram',
            'whatsapp',
            'skype',
            'other_contact'
        ]

class AuthorLoginForm(AuthenticationForm):
    captcha = CaptchaField(label='Введите текст с картинки')