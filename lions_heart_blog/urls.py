from django.conf.urls import url
from .views import PostListView, PostDetailView, CommentCreate, AboutView, ContactView


urlpatterns = [
    url(r'^$', PostListView.as_view(), name='blog'),
    url(r'^_posts/(?P<pk>\d+)/$', PostDetailView.as_view(), name='blog_detail'),
    url(r'^_posts/(?P<post_id>\d+)/new_comment/$', CommentCreate.as_view(), name='new_comment'),
    url(r'^_about/$', AboutView.as_view(), name='about'),
    url(r'^_contacts/$', ContactView.as_view(), name='contacts'),
]
