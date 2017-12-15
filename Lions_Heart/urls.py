"""Lions_Heart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.views.static import serve
from lions_heart_app.views import HomeView, CatalogueListView, ItemDetailView
from lions_heart_blog.views import PostListView, PostDetailView, CommentCreate
from lions_heart_cart.views import add_to_cart, cart_view, cart_remove, OrderView, OrderCreate

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^catalogue/$', CatalogueListView.as_view(), name='catalogue'),
    url(r'^catalogue/collection/(?P<collection_id>\d+)/$', CatalogueListView.as_view(), name='catalogue_collection'),
    url(r'^catalogue/category/(?P<category_id>\d+)/$', CatalogueListView.as_view(), name='catalogue_category'),
    url(r'^catalogue/items/(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item'),

    url(r'^blog/$', PostListView.as_view(), name='blog'),
    url(r'^blog/posts/(?P<pk>\d+)/$', PostDetailView.as_view(), name='blog_detail'),
    url(r'^blog/posts/(?P<post_id>\d+)/new_comment/$', CommentCreate.as_view(), name='new_comment'),

    url(r'^add/(?P<item_id>\d+)/$', add_to_cart, name='add_to_cart'),
    url(r'^cart/$', cart_view, name='cart'),
    url(r'^remove/(?P<item_id>\d+)/$', cart_remove, name='cart_remove'),

    url(r'^order/$', OrderView.as_view(), name='order'),
    url(r'^create_order/$', OrderCreate.as_view(), name='new_order'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
        urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
                        ]
