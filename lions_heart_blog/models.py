from django.db import models
from lions_heart_products.models import CommonInfo
from django.utils.translation import ugettext_lazy as _


class Post(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    title = models.CharField(max_length=256, verbose_name=_('name'))
    body_text = models.TextField(blank=True, null=True, verbose_name=_('text'))
    main_image = models.ImageField(blank=True, null=True, upload_to='blog/pictures',
                                   verbose_name=_('main image'))

    def __str__(self):
        return "{}".format(self.title)


class Comment(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    author = models.CharField(max_length=256, blank=True, null=True, verbose_name=_('author'))
    comment = models.TextField(blank=True, null=True, verbose_name=_('comment'))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_('post'))

    def __str__(self):
        return "{}-{}".format(self.post, self.created)


class Image(models.Model):

    class Meta(object):
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    image = models.ImageField(upload_to='blog/pictures', verbose_name=_('image'))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_('post'))

    def __str__(self):
        return "{}-{}".format(self.image, self.post)


class CompanyInformation(models.Model):

    class Meta(object):
        verbose_name = _("Company")
        verbose_name_plural = _("Company")

    about = models.TextField(verbose_name=_('about'))
    about_title_image = models.ImageField(blank=True,
                                          null=True,
                                          upload_to='company/pictures',
                                          verbose_name=_('about_image'))
    banner_title = models.CharField(max_length=256, blank=True, null=True)


class Phone(models.Model):
    phone = models.CharField(max_length=256)
    company = models.ForeignKey(CompanyInformation, on_delete=models.CASCADE)


class Email(models.Model):
    mail = models.EmailField()
    company = models.ForeignKey(CompanyInformation, on_delete=models.CASCADE)


class Address(models.Model):
    address = models.CharField(max_length=256)
    company = models.ForeignKey(CompanyInformation, on_delete=models.CASCADE)


class CompanyImage(models.Model):

    class Meta(object):
        verbose_name = _("Diploma")
        verbose_name_plural = _("Diplomas")

    image = models.ImageField(upload_to='company/pictures', verbose_name=_('image'))
    company = models.ForeignKey(CompanyInformation, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.image)


class Banners(models.Model):

    class Meta(object):
        verbose_name = "Banner"
        verbose_name_plural = "Banners"

    image = models.ImageField(upload_to='company/pictures', verbose_name='banner')
    company = models.ForeignKey(CompanyInformation, on_delete=models.CASCADE)
    is_revived = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.image)


class Reviews(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    author = models.CharField(max_length=35, verbose_name=_('name'))
    review = models.TextField(verbose_name=_('review'))

    def __str__(self):
        return "{}-{}".format(self.created, self.author)









