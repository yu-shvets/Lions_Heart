from django.db import models
from lions_heart_products.models import CommonInfo
from django.utils.translation import ugettext_lazy as _


class Post(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = _("Пост")
        verbose_name_plural = _("Посты")

    title = models.CharField(max_length=256, verbose_name=_('наименование'))
    body_text = models.TextField(blank=True, null=True, verbose_name=_('содержание'))
    main_image = models.ImageField(blank=True, null=True, upload_to='blog/pictures',
                                   verbose_name=_('титульное изображение'))

    def __str__(self):
        return "{}".format(self.title)


class Comment(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = _("Комментарий")
        verbose_name_plural = _("Комментарии")

    author = models.CharField(max_length=256, blank=True, null=True, verbose_name=_('автор'))
    comment = models.TextField(blank=True, null=True, verbose_name=_('комментарий'))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_('пост'))

    def __str__(self):
        return "{}-{}".format(self.post, self.created)


class Image(models.Model):

    class Meta(object):
        verbose_name = _("Изображение")
        verbose_name_plural = _("Изображения")

    image = models.ImageField(upload_to='blog/pictures', verbose_name=_('изображение'))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_('пост'))

    def __str__(self):
        return "{}-{}".format(self.image, self.post)


class CompanyInformation(models.Model):

    class Meta(object):
        verbose_name = _("Компания")
        verbose_name_plural = _("Компания")

    about = models.TextField(verbose_name=_('информация о компании'))
    phone = models.CharField(max_length=256, verbose_name=_('телефон'))
    mail = models.EmailField()
    address = models.CharField(max_length=256, verbose_name=_('адрес'))


class CompanyImage(models.Model):

    class Meta(object):
        verbose_name = _("Изображение")
        verbose_name_plural = _("Изображения")

    image = models.ImageField(upload_to='company/pictures', verbose_name=_('изображение'))
    company = models.ForeignKey(CompanyInformation, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.image)













