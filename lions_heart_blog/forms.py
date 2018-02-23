from django.forms import ModelForm
from .models import Comment, Reviews
from captcha.fields import CaptchaField


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'comment']


class ReviewForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Reviews
        fields = '__all__'
