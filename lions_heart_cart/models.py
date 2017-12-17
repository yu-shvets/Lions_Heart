from django.db import models
from lions_heart_products.models import CommonInfo, Item


class Order(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    PAYMENT_CHOICES = (('Карта', 'Карта'),
                        ('Наличные', 'Наличные'))

    customer_name = models.CharField(max_length=256, verbose_name="имя покупателя")
    customer_email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=13, verbose_name='телефон')
    payment_type = models.CharField(choices=PAYMENT_CHOICES, max_length=8,
                                    default='Карта', verbose_name='способ платежа')
    comment = models.TextField(verbose_name='комментарий', blank=True, null=True)
    total_cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='общая_стоимость')

    def __str__(self):
        return '{}-{}'.format(self.customer_name, self.created)


class OrderItem(models.Model):

    class Meta(object):
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"

    item = models.ForeignKey(Item, verbose_name='товар', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='количество')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='цена')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='заказ')

    def __str__(self):
        return '{}-{}'.format(self.item, self.order)

