from django.db import models


def upload(instanse, tttttt):
    return 'media/post'


class Post(models.Model):

    class Meta(object):
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ('-post_date',)

    post_date = models.DateTimeField(auto_now_add=True)

    title = models.CharField(max_length=256, verbose_name='наименование')

    slug = models.SlugField(blank=True, null=True)

    bodytext = models.TextField(blank=True, null=True, verbose_name='содержание')

    main_image = models.ImageField(blank=True, null=True, upload_to='media', verbose_name='титульное изображение')

    def __str__(self):
        return "{}".format(self.title)


class Comment(models.Model):

    class Meta(object):
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['-post_date']

    post_date = models.DateTimeField(auto_now_add=True)

    author = models.CharField(max_length=256, blank=True, null=True, verbose_name='автор')

    comment = models.TextField(blank=True, null=True, verbose_name='комментарий')

    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='пост')

    def __str__(self):
        return "{}".format(self.post_date)


class Image(models.Model):

    class Meta(object):
        verbose_name = "Изображение"
        verbose_name_plural = "изображения"

    image = models.ImageField(upload_to='media', verbose_name='титульное изображение')

    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='пост')

    def __str__(self):
        return "{}-{}".format(self.post, self.image)







