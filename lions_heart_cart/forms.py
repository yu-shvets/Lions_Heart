from django import forms
from django.forms import ModelForm
from .models import Order


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Количество', widget=forms.TextInput(attrs={
        'class': 'update_q'
    }), initial=1)


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ('customer_name', 'customer_email', 'phone', 'payment_type', 'comment')


