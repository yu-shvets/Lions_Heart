from django import forms
from django.forms import ModelForm
from .models import Order
from django.utils.translation import ugettext as _


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label=_('Quantity:'), widget=forms.TextInput(attrs={
        'class': 'update_q'
    }), initial=1)


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ('customer_name', 'customer_email', 'phone', 'payment_type', 'comment')


