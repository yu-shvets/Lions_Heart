from django import template
from decimal import *

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


@register.filter
def convert(value):
    from lions_heart_products.currency_rates import rate
    return Decimal(float(value) * rate).quantize(Decimal('.00'))
