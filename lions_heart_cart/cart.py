from decimal import Decimal
from django.conf import settings
from lions_heart_products.models import Item
from lions_heart_products.templatetags.mytemplatetags import get_rate


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, item):
        item_id = str(item.id)
        if item_id not in self.cart:
            self.cart[item_id] = {'quantity': 1, 'price': str(float(item.price) * get_rate())}
        else:
            self.cart[item_id]['quantity'] += 1
        self.save()

    def add_size(self, item, price):
        item_id = str(item.id)
        if item_id not in self.cart:
            self.cart[item_id] = {'quantity': 1, 'price': str(float(price) * get_rate())}
        else:
            self.cart[item_id]['quantity'] += 1
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, item):
        item_id = str(item.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def update(self, item, quantity):
        item_id = str(item.id)
        self.cart[item_id]['quantity'] = quantity
        self.save()

    def __iter__(self):
        item_ids = self.cart.keys()
        items = Item.objects.filter(id__in=item_ids)
        for item in items:
            self.cart[str(item.id)]['item'] = item

        for item in self.cart.values():
            item['price'] = Decimal(item['price']).quantize(Decimal('.00'))
            item['total_price'] = item['price'] * item['quantity']
            yield item

    @property
    def cart_len(self):
        return sum(item['quantity'] for item in self.cart.values())

    def sum_item(self, item, quantity):
        item_id = str(item.id)
        return Decimal(self.cart[item_id]['price']).quantize(Decimal('.00')) * quantity

    def get_total_price(self):
        return sum(Decimal(item['price']).quantize(Decimal('.00')) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
