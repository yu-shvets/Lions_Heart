from django.forms import ModelForm
from .models import Comment, Reviews


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'comment']


class ReviewForm(ModelForm):

    class Meta:
        model = Reviews
        fields = ['author', 'review']
