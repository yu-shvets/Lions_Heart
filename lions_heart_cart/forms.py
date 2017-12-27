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
        fields = ('customer_name', 'customer_email', 'phone', 'payment_type', 'comment')
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form__field form__field_main form__field_black'}),
            'customer_email': forms.EmailInput(attrs={'class': 'form__field form__field_main form__field_black'}),
            'phone': forms.TextInput(attrs={'class': 'form__field form__field_main form__field_black'}),
            'comment': forms.TextInput(attrs={'class': 'form__field form__field_main form__field_black'}),
        }


