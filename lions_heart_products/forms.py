from django import forms


# class SizesForm(forms.Form):
#
#     def __init__(self, pk, *args, **kwargs):
#         super(SizesForm, self).__init__(*args, **kwargs)
#         self.fields['size'] = forms.ChoiceField(choices=[(i.size, str(i.size)) for i in Sizes.objects.filter(item=pk)])
