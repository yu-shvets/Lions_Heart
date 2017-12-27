from django.db import models
from lions_heart_products.models import CommonInfo, Item
from django.utils.translation import ugettext_lazy as _


class Order(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    PAYMENT_CHOICES = ((_('Credit card'), _('Credit card')),
                       (_('Cash'), _('Cash')))

    customer_name = models.CharField(max_length=256, verbose_name=_("name"))
    customer_email = models.EmailField(verbose_name="email")
    phone = models.CharField(max_length=13, verbose_name=_('phone'))
    payment_type = models.CharField(choices=PAYMENT_CHOICES, max_length=11,
                                    default='Карта', verbose_name=_('payment type'))
    comment = models.TextField(verbose_name=_('comment'), blank=True, null=True)
    total_cost = models.DecimalField(max_digits=11, decimal_places=2, verbose_name=_('total cost'))

    def __str__(self):
        return '{}-{}'.format(self.customer_name, self.created)


class OrderItem(models.Model):

    class Meta(object):
        verbose_name = _("Item in order")
        verbose_name_plural = _("Items in orders")

    item = models.ForeignKey(Item, verbose_name=_('Item'), on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name=_('quantity'))
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name=_('price'))
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_('order'))

    def __str__(self):
        return '{}-{}'.format(self.item, self.order)

