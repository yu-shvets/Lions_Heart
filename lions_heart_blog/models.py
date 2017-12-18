from django.db import models
from lions_heart_products.models import CommonInfo


class Post(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    title = models.CharField(max_length=256, verbose_name='наименование')
    body_text = models.TextField(blank=True, null=True, verbose_name='содержание')
    main_image = models.ImageField(blank=True, null=True, upload_to='blog/pictures',
                                   verbose_name='титульное изображение')

    def __str__(self):
        return "{}".format(self.title)


class Comment(CommonInfo):

    class Meta(CommonInfo.Meta):
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    author = models.CharField(max_length=256, blank=True, null=True, verbose_name='автор')
    comment = models.TextField(blank=True, null=True, verbose_name='комментарий')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='пост')

    def __str__(self):
        return "{}-{}".format(self.post, self.created)


class Image(models.Model):

    class Meta(object):
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    image = models.ImageField(upload_to='blog/pictures', verbose_name='изображение')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='пост')

    def __str__(self):
        return "{}-{}".format(self.image, self.post)


class CompanyInformation(models.Model):

    class Meta(object):
        verbose_name = "Компания"
        verbose_name_plural = "Компания"

    about = models.TextField(verbose_name='информация о компании')
    phone = models.CharField(max_length=256, verbose_name='телефон')
    mail = models.EmailField()
    address = models.CharField(max_length=256, verbose_name='адрес')


class CompanyImage(models.Model):

    class Meta(object):
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    image = models.ImageField(upload_to='company/pictures', verbose_name='изображение')
    company = models.ForeignKey(CompanyInformation, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.image)













