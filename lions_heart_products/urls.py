from django.conf.urls import url
from .views import HomeView, CatalogueListView, ItemDetailView, WomenLisView, MenListView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^catalogue/$', CatalogueListView.as_view(), name='catalogue'),
    url(r'^catalogue/collection/(?P<collection_id>\d+)/$', CatalogueListView.as_view(), name='catalogue_collection'),
    url(r'^catalogue/category/(?P<category_id>\d+)/$', CatalogueListView.as_view(), name='catalogue_category'),
    url(r'^catalogue/items/(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item'),

    url(r'^catalogue/items/women/(?P<collection_id>\d+)/$', WomenLisView.as_view(), name='women'),
    url(r'^catalogue/items/men/(?P<collection_id>\d+)/$', MenListView.as_view(), name='men'),
                ]
