from django.conf.urls import url
from .views import PostListView, PostDetailView, CommentCreate


urlpatterns = [
    url(r'^$', PostListView.as_view(), name='blog'),
    url(r'^posts/(?P<pk>\d+)/$', PostDetailView.as_view(), name='blog_detail'),
    url(r'^posts/(?P<post_id>\d+)/new_comment/$', CommentCreate.as_view(), name='new_comment'),
]
