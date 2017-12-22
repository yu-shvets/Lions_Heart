from django.conf.urls import url
from .views import HomeView, CollectionListView, CategoryListView,  ItemDetailView, CollectionDetailView, \
    collection_category, women_collection, men_collection, product_list

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^catalogue/$', product_list, name='catalogue'),

    url(r'^catalogue/collection/(?P<pk>\d+)/$', CollectionDetailView.as_view(), name='catalogue_collection'),

    url(r'^catalogue/collection/(?P<collection_id>\d+)/category/(?P<category_id>\d+)/$', collection_category,
        name='collection_category'),

    url(r'^catalogue/collection/(?P<collection_id>\d+)/women/$', women_collection, name='women'),
    url(r'^catalogue/collection/(?P<collection_id>\d+)/men/$', men_collection, name='men'),

    url(r'^catalogue/category/(?P<category_id>\d+)/$', CategoryListView.as_view(), name='catalogue_category'),
    url(r'^catalogue/items/(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item'),

    # url(r'^catalogue/items/women/(?P<collection_id>\d+)/$', WomenListView, name='women'),
    # url(r'^catalogue/items/men/(?P<collection_id>\d+)/$', MenListView.as_view(), name='men'),
                ]
