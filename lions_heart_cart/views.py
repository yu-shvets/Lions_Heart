from django.shortcuts import render, reverse, HttpResponseRedirect, redirect, get_object_or_404
from .cart import Cart
from lions_heart_products.models import Item
from django.shortcuts import get_object_or_404
from .models import Order, OrderItem
from .forms import CartAddProductForm, OrderForm
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.core.mail import send_mail
from django.conf import settings
from libs.liqpay import LiqPay
from lions_heart_products.models import Item


def check_recommended(cart):
    for i in cart:
        if i['item'].recommended_items.all():
            return True
    return False


def cart_view(request):
    cart = Cart(request)
    recommended = check_recommended(cart)
    total_price = cart.get_total_price()
    form = CartAddProductForm()
    return render(request, 'lions_heart_cart/cart.html', {'cart': cart, 'total_price': total_price,
                                                          'form': form, 'recommended': recommended})


def add_to_cart(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.add(item=item)
    messages.success(request, _('The item was successfully added to cart'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.remove(item)
    return HttpResponseRedirect(reverse('cart'))


def update_quantity(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    response_data = {}
    if request.method == 'POST':
        new_quantity = (request.POST['new_quantity'])
        if new_quantity.isnumeric():
            new_quantity = int(new_quantity)
            if 0 < new_quantity <= 100:
                cart.update(item, new_quantity)
                response_data['quantity'] = new_quantity
                response_data['sum'] = cart.sum_item(item, new_quantity)
                response_data['total_price'] = cart.get_total_price()
    return JsonResponse(response_data)


class OrderView(TemplateView):
    template_name = 'lions_heart_cart/order.html'

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        context['form'] = OrderForm()
        return context


def liqpay(amount, order_id):
    liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
    html = liqpay.cnb_form({
    'action': 'pay',
    'amount': str(amount),
    'currency': 'UAH',
    'description': 'Payment for jewelry',
    'order_id': str(order_id),
    })
    return html


class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'lions_heart_cart/order.html'

    def form_valid(self, form):
        cart = Cart(self.request)
        self.obj = form.save(commit=False)
        self.obj.total_cost = cart.get_total_price()
        self.obj.save()
        message = 'New order #{}\n\n'.format(self.obj.id)
        for element in cart:
            order_item = OrderItem(item=element['item'], quantity=element['quantity'],
                                   price=element['price'], order=self.obj)
            order_item.save()
            message += str(element['item']) + ' ' + '-' + ' ' + str(element['quantity'])+ 'pcs' + ' ' + '-' + ' ' + str(element['price']) + 'UAH' + '\n\n'
        cart.clear()
        message += 'Total cost - {}'.format(self.obj.total_cost)
        send_mail('Lions Heart', message, settings.EMAIL_HOST_USER, [self.obj.customer_email])
        if self.obj.payment_type == 'Cash' or self.obj.payment_type == 'Наличные':
            return HttpResponseRedirect(reverse('success'))
        else:
            if self.obj.total_cost:
                data = liqpay(amount=self.obj.total_cost, order_id=self.obj.id)
                return render(self.request, 'lions_heart_cart/pay.html', {'data': data})
            else:
                return HttpResponseRedirect(reverse('cart'))


class PayView(TemplateView):
    template_name = 'lions_heart_cart/pay.html'


class SuccessView(TemplateView):
    template_name = 'lions_heart_cart/order_success.html'


# def add_cart_size(request, sizes_id):
#     cart = Cart(request)
#     size = get_object_or_404(Sizes, id=sizes_id)
#     cart.add_size(item=size.item, price=size.price)
#     messages.success(request, _('The item was successfully added to cart'))
#     return HttpResponseRedirect(reverse('home'))


# def update_quantity(request, item_id):
#     cart = Cart(request)
#     item = get_object_or_404(Item, id=item_id)
#     form = CartAddProductForm(data=request.POST)
#     response_data = {}
#     if form.is_valid():
#         data = form.cleaned_data
#         new_quantity = data['quantity']
#         cart.update(item, new_quantity)
#         response_data['quantity'] = new_quantity
#         response_data['sum'] = new_quantity * item.price
#         response_data['total_price'] = cart.get_total_price()
#     return JsonResponse(response_data)
