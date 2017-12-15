from django.db import models
from lions_heart_app.models import Item


class Order(models.Model):

    class Meta(object):
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    PAYMENT_CHOICES = (('Карта', 'Карта'),
                        ('Наличные', 'Наличные'))

    created = models.DateTimeField(auto_now_add=True)

    customer_name = models.CharField(max_length=256, verbose_name="имя покупателя")

    customer_email = models.EmailField(verbose_name="Email")

    phone = models.CharField(max_length=13, verbose_name='телефон')

    payment_type = models.CharField(choices=PAYMENT_CHOICES, max_length=8,
                                    default='Карта', verbose_name='способ платежа')

    comment = models.TextField(verbose_name='комментарий', blank=True, null=True)

    total_cost = models.FloatField(blank=True, null=True, verbose_name='общая_стоимость')

    def __str__(self):
        return '{}-{}'.format(self.customer_name, self.created)


class OrderItem(models.Model):

    class Meta(object):
        verbose_name = "Товар в заказе"
        verbose_name_plural = "Товары в заказе"

    item = models.ForeignKey(Item, verbose_name='товар', on_delete=models.CASCADE)

    quantity = models.IntegerField(verbose_name='количество')

    price = models.FloatField(blank=True, null=True, verbose_name='цена')

    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='заказ')

    def get_price(self):
        return self.item.price

    def __str__(self):
        return '{}'.format(self.order)

