from django import forms
from .models import Collection, Category, Item


class SearchForm(forms.Form):

    collection = forms.ChoiceField(queryset= Collection.objects.all(), widget=forms.CheckboxInput)
    category = forms.ChoiceField(queryset= Category.objects.all(), widget=forms.CheckboxInput)
    type = forms.ChoiceField(choices=Item.TYPE_CHOICES, widget=forms.CheckboxInput)