from django.conf.urls import url
from lions_heart_billing.views import PayView, PayCallbackView, liqpay


urlpatterns = [
    url(r'^pay/$', liqpay, name='pay_view'),
    url(r'^pay-callback/$', PayCallbackView.as_view(), name='pay_callback'),
]