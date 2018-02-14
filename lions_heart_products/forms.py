from django import forms
from .models import Attributes


class AttributesForm(forms.Form):

    def __init__(self, pk, *args, **kwargs):
        super(AttributesForm, self).__init__(*args, **kwargs)
        self.fields['size'] = forms.ChoiceField(
            choices=[(i.size, str(i.size)) for i in Attributes.objects.filter(item=pk)])


