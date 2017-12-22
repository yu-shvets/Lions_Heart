from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import ugettext_lazy as _


class CommonInfo(models.Model):

    class Meta:
        abstract = True
        ordering = ['-created']

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Category(MPTTModel):

    class Meta(object):
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")

    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=256, verbose_name=_('наименование'))
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children',
                            db_index=True, on_delete=models.CASCADE, verbose_name=_('родительская категория'))

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return "{}".format(self.title)


class Collection(models.Model):

    class Meta(object):
        verbose_name = _("Коллекция")
        verbose_name_plural = _("Коллекции")

    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=256, verbose_name=_('наименование'))
    logo_image = models.ImageField(upload_to='collection/logos', verbose_name=_('логотип коллекции'),
                                   blank=True, null=True)
    description = models.TextField(verbose_name=_('описание коллекции'), blank=True, null=True)

    def __str__(self):
        return "{}".format(self.title)


class Item(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = _("Товар")
        verbose_name_plural = _("Товары")

    TYPE_CHOICES = ((_('Мужская'), _('Мужская')),
                    (_('Женская'), _('Женская')))

    title = models.CharField(max_length=256, verbose_name=_('наименование'))
    title_image = models.ImageField(upload_to='catalog/products', verbose_name=_('титульное изображение'))
    description = models.TextField(blank=True, null=True, verbose_name=_('описание'))
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name=_('цена'))
    slug = models.SlugField(blank=True, null=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=7, default=_('Женская'), verbose_name=_('тип коллекции'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('категория'))
    collection = models.ForeignKey(Collection, null=True, on_delete=models.CASCADE, verbose_name=_('коллекция'))
    recommended_items = models.ManyToManyField('self', blank=True, verbose_name=_('рекомендованные товары'))

    def __str__(self):
        return "{}-{}".format(self.category, self.title)


class Image(models.Model):

    class Meta(object):
        verbose_name = _("Изображение")
        verbose_name_plural = _("Изображения")

    image = models.ImageField(upload_to='catalog/products', verbose_name=_('изображение'))
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name=_('товар'))

    def __str__(self):
        return "{}-{}".format(self.item, self.image)


class Specs(models.Model):

    class Meta(object):
        verbose_name = _("Характекристика изделия")
        verbose_name_plural = _("Характекристики изделия")

    weight = models.FloatField(blank=True, null=True, verbose_name=_('вес, гр'))
    diameter = models.FloatField(blank=True, null=True, verbose_name=_('диаметр, мм'))
    length = models.FloatField(blank=True, null=True, verbose_name=_('длина, мм'))
    specs = models.TextField(blank=True, null=True, verbose_name=_('прочие характекристики'))
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
