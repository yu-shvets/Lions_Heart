from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class CommonInfo(models.Model):

    class Meta:
        abstract = True
        ordering = ['-created']

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Category(MPTTModel):

    class Meta(object):
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=256, verbose_name='наименование')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children',
                            db_index=True, on_delete=models.CASCADE, verbose_name='родительская категория')

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return "{}".format(self.title)


class Collection(models.Model):

    class Meta(object):
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"

    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=256, verbose_name='наименование')
    logo_image = models.ImageField(upload_to='collection/logos', verbose_name='логотип коллекции',
                                   blank=True, null=True)
    description = models.TextField(verbose_name='описание коллекции', blank=True, null=True)

    def __str__(self):
        return "{}".format(self.title)


class Item(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    TYPE_CHOICES = (('Мужская', 'Мужская'),
                    ('Женская', 'Женская'))

    title = models.CharField(max_length=256, verbose_name='наименование')
    title_image = models.ImageField(upload_to='catalog/products', verbose_name='титульное изображение')
    description = models.TextField(blank=True, null=True, verbose_name='описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='цена')
    slug = models.SlugField(blank=True, null=True)
    type = models.CharField(choices=TYPE_CHOICES, max_length=7, default='Женская', verbose_name='тип коллекции')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    collection = models.ForeignKey(Collection, null=True, on_delete=models.CASCADE, verbose_name='коллекция')
    recommended_items = models.ManyToManyField('self', blank=True, verbose_name='рекомендованные товары')

    def __str__(self):
        return "{}-{}".format(self.category, self.title)


class Image(models.Model):

    class Meta(object):
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    image = models.ImageField(upload_to='catalog/products', verbose_name='изображение')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='товар')

    def __str__(self):
        return "{}-{}".format(self.item, self.image)


class Specs(models.Model):

    class Meta(object):
        verbose_name = "Характеристика товара"
        verbose_name_plural = "Характекристики товара"

    weight = models.FloatField(blank=True, null=True, verbose_name='вес')
    specs = models.TextField(verbose_name='характекристики товара')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='товар')

    def __str__(self):
        return "{}".format(self.item)


