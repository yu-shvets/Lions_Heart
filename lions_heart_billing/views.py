from libs.liqpay import LiqPay
from django.views.generic import View, TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class PayView(TemplateView):
    template_name = 'lions_heart_billing/pay.html'

    def get(self, request, *args, **kwargs):
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        params = {
            'action': 'pay',
            'amount': '100',
            'currency': 'USD',
            'description': 'Payment for clothes',
            'order_id': 'order_id_1',
            'version': '3',
            'sandbox': 0,  # sandbox mode, set to 1 to enable it
            'server_url': '', # url to callback view
        }
        signature = liqpay.cnb_signature(params)
        data = liqpay.cnb_form(params)

        print(data)
        return render(request, self.template_name, {'signature': signature, 'data': data})




@method_decorator(csrf_exempt, name='dispatch')
class PayCallbackView(View):
    def post(self, request, *args, **kwargs):
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        data = request.POST.get('data')
        signature = request.POST.get('signature')
        sign = liqpay.str_to_sign(settings.LIQPAY_PRIVATE_KEY + data + settings.LIQPAY_PRIVATE_KEY)
        if sign == signature:
            print('callback is valid')
        response = liqpay.decode_data_from_str(data)
        print('callback data', response)
        return HttpResponse()


def liqpay(request):
    liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
    html = liqpay.cnb_form({
    'action': 'pay',
    'amount': '1',
    'currency': 'UAH',
    'description': 'Payment for jewelry',
    'order_id': 'order_id_1',
    })
    return render(request, 'lions_heart_billing/pay.html', {'data': html})
