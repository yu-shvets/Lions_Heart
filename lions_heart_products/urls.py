from django.conf.urls import url
from .views import HomeView, ItemDetailView, CollectionListView, CategoryCollectionListView, \
    CategoryListView, CollectionCategoryListView, SalesCollectionListView, SalesListView, \
    CollectionSalesListView, UniqueGiftsListView, CollectionUniqueGiftsListView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^catalogue/categories/(?P<category_id>\d+)/$', CategoryListView.as_view(), name='category'),
    url(r'^catalogue/categories/(?P<category_id>\d+)/collections/(?P<collection_id>\d+)/$',
        CollectionCategoryListView.as_view(), name='category_collection'),

    url(r'^catalogue/sales/$', SalesListView.as_view(), name='sales'),
    url(r'^catalogue/sales/collection/(?P<collection_id>\d+)/$',
        CollectionSalesListView.as_view(), name='sales_collection'),

    url(r'^catalogue/collections/(?P<collection_id>\d+)/$', CollectionListView.as_view(), name='collection'),
    url(r'^catalogue/collections/(?P<collection_id>\d+)/categories/(?P<category_id>\d+)/$',
        CategoryCollectionListView.as_view(), name='collection_category'),
    url(r'^catalogue/collections/(?P<collection_id>\d+)/sales/$',
        SalesCollectionListView.as_view(), name='collection_sales'),

    url(r'^unique_gifts/$', UniqueGiftsListView.as_view(), name='gifts'),
    url(r'^unique_gifts/collection/(?P<collection_id>\d+)/$',
        CollectionUniqueGiftsListView.as_view(), name='gifts_collection'),

    url(r'^catalogue/items/(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item'),
                ]
