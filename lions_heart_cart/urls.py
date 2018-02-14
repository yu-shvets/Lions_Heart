from django.conf.urls import url
from .views import add_to_cart_catalogue, add_to_cart_size, cart_view, cart_remove, update_quantity, \
    OrderView, OrderCreate, SuccessView, PayView


urlpatterns = [
    url(r'^add/(?P<item_id>\d+)/$', add_to_cart_catalogue, name='add_to_cart'),
    url(r'^add_item/$', add_to_cart_size, name='add_item'),
    url(r'^cart/$', cart_view, name='cart'),
    url(r'^remove/(?P<attributes_id>\d+)/$', cart_remove, name='cart_remove'),
    url(r'^update/(?P<attributes_id>\d+)/$', update_quantity, name='cart_update'),

    url(r'^order/$', OrderView.as_view(), name='order'),
    url(r'^create_order/$', OrderCreate.as_view(), name='new_order'),

    url(r'^pay/$', PayView.as_view(), name='pay'),

    url(r'^order_success/$', SuccessView.as_view(), name='success'),
                ]
