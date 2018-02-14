from django.conf import settings
from lions_heart_products.models import Attributes
from lions_heart_products.templatetags.mytemplatetags import get_rate
from decimal import *


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, attributes_id):
        if attributes_id not in self.cart:
            self.cart[attributes_id] = {'quantity': 1}
        else:
            self.cart[attributes_id]['quantity'] += 1
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, attributes_id):
        if attributes_id in self.cart:
            del self.cart[attributes_id]
            self.save()

    def update(self, attributes_id, quantity):
        self.cart[attributes_id]['quantity'] = quantity
        self.save()

    def __getitem__(self, key):
        return self.cart[key]

    def __iter__(self):
        for item in self.cart.keys():
            yield item

    def item_sum(self, attributes_id):
        attributes = Attributes.objects.get(id=int(attributes_id))
        quantity = self.cart[attributes_id]['quantity']
        if attributes.sales_price:
            value = attributes.sales_price
        else:
            value = attributes.price
        return Decimal(round(float(value * quantity) * get_rate())).quantize(Decimal('.00'))

    def get_total(self):
        total = 0
        for item in self.cart:
            attributes = Attributes.objects.get(id=int(item))
            quantity = self.cart[item]['quantity']
            if attributes.sales_price:
                total += attributes.sales_price * quantity
            else:
                total += attributes.price * quantity
        return Decimal(round(float(total) * get_rate())).quantize(Decimal('.00'))

    def cart_len(self):
        return len([item for item in self.cart])

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
