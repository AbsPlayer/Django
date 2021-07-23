from django import forms
from advertisements.models import Advertisement


class AdvertisementForm(forms.ModelForm):
    photo = forms.ImageField(required=False)

    class Meta:
        model = Advertisement
        fields = [
            'title',
            'description',
            'price',
            'photo',
            'type',
            'rubric',
        ]


class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=20, required=False, label='')
