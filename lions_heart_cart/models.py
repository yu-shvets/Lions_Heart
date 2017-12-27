from django.db import models
from lions_heart_products.models import CommonInfo, Item
from django.utils.translation import ugettext_lazy as _


class Order(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = _("Заказ")
        verbose_name_plural = _("Заказы")

    PAYMENT_CHOICES = ((_('Карта'), _('Карта')),
                       (_('Наличные'), _('Наличные')))

    customer_name = models.CharField(max_length=256, verbose_name=_("имя покупателя"))
    customer_email = models.EmailField(verbose_name="email")
    phone = models.CharField(max_length=13, verbose_name=_('телефон'))
    payment_type = models.CharField(choices=PAYMENT_CHOICES, max_length=11,
                                    default='Карта', verbose_name=_('способ платежа'))
    comment = models.TextField(verbose_name=_('комментарий'), blank=True, null=True)
    total_cost = models.DecimalField(max_digits=11, decimal_places=2, verbose_name=_('общая_стоимость'))

    def __str__(self):
        return '{}-{}'.format(self.customer_name, self.created)


class OrderItem(models.Model):

    class Meta(object):
        verbose_name = _("Товар в заказе")
        verbose_name_plural = _("Товары в заказе")

    item = models.ForeignKey(Item, verbose_name=_('товар'), on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name=_('количество'))
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name=_('цена'))
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_('заказ'))

    def __str__(self):
        return '{}-{}'.format(self.item, self.order)

