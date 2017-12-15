from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.db import transaction


class Category(MPTTModel):

    class Meta(object):
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

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

    title = models.CharField(max_length=256, verbose_name='наименование')

    def __str__(self):
        return "{}".format(self.title)


class Item(models.Model):

    class Meta(object):
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-created']

    TYPE_CHOICES = (('Мужская', 'Мужская'),
                   ('Женская', 'Женская'))

    created = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=256, verbose_name='наименование')

    description = models.TextField(blank=True, null=True, verbose_name='описание')

    price = models.FloatField(verbose_name='цена')

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

    image = models.ImageField(upload_to='media', verbose_name='изображение')

    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='товар')

    main_image = models.BooleanField(default=False, verbose_name='титульное изображение')

    '''@transaction.atomic
    def save(self, *args, **kwargs):
        if self.main_image:
            Image.objects.filter(
                main_image=True).update(main_image=False)
        super(Image, self).save(*args, **kwargs)'''

    def __str__(self):
        return "{}-{}".format(self.item, self.image)


class Specs(models.Model):

    class Meta(object):
        verbose_name = "Характеристика товара"
        verbose_name_plural = "Характекристики товара"

    specs = models.TextField(verbose_name='характекристики товара')

    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='товар')

    def __str__(self):
        return "{}".format(self.item)

