from django.conf.urls import url
from .views import HomeView, itemlistview, ItemDetailView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^catalogue/$', itemlistview, name='catalogue'),
    url(r'^catalogue/items/(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item'),
                ]
