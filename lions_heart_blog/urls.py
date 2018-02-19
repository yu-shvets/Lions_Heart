from django.conf.urls import url
from .views import PostListView, PostDetailView, CommentCreate, AboutView, ContactView, ReviewsListView, ReviewCreate


urlpatterns = [
    url(r'^blog/$', PostListView.as_view(), name='blog'),
    url(r'^blog_posts/(?P<pk>\d+)/$', PostDetailView.as_view(), name='blog_detail'),
    url(r'^blog_posts/(?P<post_id>\d+)/new_comment/$', CommentCreate.as_view(), name='new_comment'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contacts/$', ContactView.as_view(), name='contacts'),
    url(r'^reviews/$', ReviewsListView.as_view(), name='reviews'),
    url(r'^review_create/$', ReviewCreate.as_view(), name='review_create'),
]
