from django.conf.urls import url
from .views import HomeView, ItemFilterView, ItemDetailView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^catalogue/$', ItemFilterView.as_view(), name='catalogue'),
    url(r'^catalogue/items/(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item'),
                ]
