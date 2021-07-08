from django import forms

from .models import StoriesDetail


class StoriesDetailForm(forms.ModelForm):
    class Meta:
        model = StoriesDetail
        fields = '__all__'
        exclude = ('id',)
