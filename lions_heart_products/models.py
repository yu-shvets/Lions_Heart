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
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=256, verbose_name=_('title'))
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children',
                            db_index=True, on_delete=models.CASCADE, verbose_name=_('parent сategory'))

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return "{}".format(self.title)


class Collection(models.Model):

    class Meta(object):
        verbose_name = _("Сollection")
        verbose_name_plural = _("Сollections")

    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=256, verbose_name=_('name'))
    logo_image = models.ImageField(upload_to='collection/logos', verbose_name=_('logo'),
                                   blank=True, null=True)
    description = models.TextField(verbose_name=_('description'), blank=True, null=True)

    def __str__(self):
        return "{}".format(self.title)


class Item(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = _("Item")
        verbose_name_plural = _("Items")

    TYPE_CHOICES = ((_('Men'), _('Men')),
                    (_('Women'), _('Women')))

    title = models.CharField(max_length=256, verbose_name=_('name'))
    title_image = models.ImageField(upload_to='catalog/products', verbose_name=_('title image'))
    description = models.TextField(blank=True, null=True, verbose_name=_('description'))
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name=_('price'))
    slug = models.SlugField(blank=True, null=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=7, default=_('Women'), verbose_name=_('type'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('сategory'))
    collection = models.ForeignKey(Collection, null=True, on_delete=models.CASCADE, verbose_name=_('сollection'))
    recommended_items = models.ManyToManyField('self', blank=True, verbose_name=_('recommended'))
    sales = models.IntegerField(verbose_name=_('sales'), blank=True, null=True)
    unique_gift = models.BooleanField(default=False, verbose_name=_('unique gift'))

    def __str__(self):
        return "{}-{}".format(self.category, self.title)


class Image(models.Model):

    class Meta(object):
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    image = models.ImageField(upload_to='catalog/products', verbose_name=_('image'))
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name=_('item'))

    def __str__(self):
        return "{}-{}".format(self.item, self.image)


class Specs(models.Model):

    class Meta(object):
        verbose_name = _("Specs")
        verbose_name_plural = _("Specs")

    weight = models.FloatField(blank=True, null=True, verbose_name=_('weight, gr'))
    diameter = models.FloatField(blank=True, null=True, verbose_name=_('diameter, mm'))
    length = models.FloatField(blank=True, null=True, verbose_name=_('length, mm'))
    specs = models.TextField(blank=True, null=True, verbose_name=_('other specs'))
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
