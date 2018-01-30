from django import template
from decimal import *
from lions_heart_products.models import CurrencyRate
import datetime
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.simple_tag
def url_replace(request, field, value):
    d = request.GET.copy()
    d[field] = value
    return d.urlencode()


@register.simple_tag
def url_delete(request, field):
    d = request.GET.copy()
    del d[field]
    return d.urlencode()


def post_rate():
    from lions_heart_products.currency_rates import request_rate
    rate = request_rate()
    return CurrencyRate(rate=rate).save()


def get_rate():
    try:
        rate = CurrencyRate.objects.get(created__date=datetime.date.today()).rate
    except ObjectDoesNotExist:
        post_rate()
        rate = CurrencyRate.objects.get(created__date=datetime.date.today()).rate

    return rate


@register.filter
def convert(value):
    rate = get_rate()
    return Decimal(round(float(value) * rate)).quantize(Decimal('.00'))

