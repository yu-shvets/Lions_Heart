from django import template
from decimal import *
from lions_heart_products.models import CurrencyRate
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse

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
    if rate:
        CurrencyRate(rate=rate).save()
        return rate
    return CurrencyRate.objects.filter().first().rate


def get_rate():
    try:
        rate = CurrencyRate.objects.get(created__date=datetime.date.today()).rate
    except ObjectDoesNotExist:
        rate = post_rate()
    return rate


@register.filter
def convert(value):
    rate = get_rate()
    return Decimal(round(float(value) * rate)).quantize(Decimal('.00'))


@register.simple_tag
def get_category(route_name, request, first_id=None, second_id=None):
    route = reverse(route_name, kwargs={'collection_id': first_id, 'category_id': second_id})
    if second_id and request.path == route:
        return "<a class='catalog__menu catalog__menu_active nav__link_capitalize' href=//{}{}>".format(request.get_host(), route)
    return "<a class='catalog__menu nav__link_capitalize' href=//{}{}>".format(request.get_host(), route)
