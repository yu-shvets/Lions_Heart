from django.conf.urls import url
from .views import HomeView, ItemDetailView, CollectionListView, CategoryCollectionListView, \
    SalesListView, CollectionSalesListView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^catalogue/collections/(?P<collection_id>\d+)/$', CollectionListView.as_view(), name='collection'),
    url(r'^catalogue/collections/(?P<collection_id>\d+)/categories/(?P<category_id>\d+)/$',
        CategoryCollectionListView.as_view(), name='collection_category'),

    url(r'^catalogue/sales/$', SalesListView.as_view(), name='sales'),
    url(r'^catalogue/sales/collection/(?P<collection_id>\d+)/$',
        CollectionSalesListView.as_view(), name='sales_collection'),

    url(r'^catalogue/items/(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item'),
                ]
