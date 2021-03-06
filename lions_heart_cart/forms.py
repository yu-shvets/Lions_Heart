from django import forms
from django.forms import ModelForm
from .models import Order
from django.utils.translation import ugettext as _


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='', widget=forms.TextInput(attrs={
        'class': 'update_q'}))


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ('customer_name', 'phone', 'comment')
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form__field form__field_main form__field_black ordering__position ordering__position_center'}),
            'phone': forms.TextInput(attrs={'class': 'form__field form__field_main form__field_black ordering__position ordering__position_center'}),
            'comment': forms.Textarea(attrs={'class': 'form__field form__field_black form__field_textarea ordering__position ordering__position_center'}),
        }


