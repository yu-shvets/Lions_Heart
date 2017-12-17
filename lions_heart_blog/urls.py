from django.conf.urls import url
from .views import PostListView, PostDetailView, CommentCreate

urlpatterns = [
    url(r'^blog/$', PostListView.as_view(), name='blog'),
    url(r'^blog/posts/(?P<pk>\d+)/$', PostDetailView.as_view(), name='blog_detail'),
    url(r'^blog/posts/(?P<post_id>\d+)/new_comment/$', CommentCreate.as_view(), name='new_comment'),
                ]
