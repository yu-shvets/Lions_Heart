from django.shortcuts import render, reverse, HttpResponseRedirect, redirect, get_object_or_404
from .cart import Cart
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
from lions_heart_products.models import Item, Attributes
from lions_heart_products.templatetags.mytemplatetags import convert


def get_recommended(request):
    cart_items = get_cart(request)
    products = [item['attributes'].item for item in cart_items]
    recommended = []
    for product in products:
        if product.recommended_items.all():
            for item in product.recommended_items.all():
                if item not in products and item not in recommended:
                    recommended.append(item)
    return recommended


def check_size(request):
    cart_items = get_cart(request)
    products = [item['attributes'].item for item in cart_items]
    for product in products:
        if len(product.attributes_set.all()) > 1:
            return True
    return False


def get_cart(request):
    cart_items = []
    cart = Cart(request)
    for item in cart:
        attributes = Attributes.objects.get(id=int(item))
        quantity = cart[item]['quantity']
        cart_items.append({'attributes': attributes, 'quantity': quantity,
                           'total_price': cart.item_sum(str(attributes.id))})
    return cart_items


def cart_view(request):
    cart = Cart(request)
    cart_items = get_cart(request)
    cart_total = cart.get_total()
    form = CartAddProductForm()
    recommended = get_recommended(request)
    sizes = check_size(request)
    products = [item['attributes'].item for item in cart_items]
    return render(request, 'lions_heart_cart/cart.html', {'cart_items': cart_items, 'cart_total': cart_total,
                'form': form, 'recommended': recommended, 'products': products, 'sizes': sizes})


def add_to_cart(request, attributes_id):
    cart = Cart(request)
    response_data = {}
    cart.add(attributes_id)
    response_data['items'] = cart.cart_len()
    return JsonResponse(response_data)


def add_to_cart_size(request):
    attributes_id = request.POST.get('size_id', False)
    return add_to_cart(request, attributes_id)


def add_to_cart_catalogue(request, item_id):
    item = get_object_or_404(Item, id=int(item_id))
    attributes_id = str(item.get_first_attribute().id)
    return add_to_cart(request, attributes_id)


def cart_remove(request, attributes_id):
    cart = Cart(request)
    cart.remove(attributes_id)
    return HttpResponseRedirect(reverse('cart'))


def update_quantity(request, attributes_id):
    cart = Cart(request)
    response_data = {}
    if request.method == 'POST':
        new_quantity = (request.POST['new_quantity'])
        if new_quantity.isnumeric():
            new_quantity = int(new_quantity)
            if 0 < new_quantity <= 100:
                cart.update(attributes_id, quantity=new_quantity)
                response_data['quantity'] = new_quantity
                response_data['sum'] = cart.item_sum(attributes_id)
                response_data['total_price'] = cart.get_total()
    return JsonResponse(response_data)


def update_size_cart(request, attributes_id):
    cart = Cart(request)
    if request.method == 'POST':
        new_size = request.POST['size'].replace(',', '.')
        cart.update_size(attributes_id, new_size=float(new_size))
    return HttpResponseRedirect(reverse('cart'))


class OrderView(TemplateView):
    template_name = 'lions_heart_cart/order.html'

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context['cart_items'] = get_cart(self.request)
        context['cart_total'] = Cart(self.request).get_total()
        context['form'] = OrderForm()
        return context

    def dispatch(self, request, *args, **kwargs):
        cart = Cart(self.request)
        if not cart.get_total():
            return redirect('home')
        return super(OrderView, self).dispatch(request, *args, **kwargs)


def liqpay(request, amount, order_id):
    liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
    html = liqpay.cnb_form({
    'action': 'pay',
    'amount': str(amount),
    'language': request.LANGUAGE_CODE,
    'currency': 'UAH',
    'description': 'Payment for jewelry',
    'order_id': str(order_id),
    })
    return html


def create_order_item(request, obj):
    message = 'New order #{}\n\n'.format(obj.id) + 'Name: {}\n\n'.format(obj.customer_name) + \
              'E-mail: {}\n\n'.format(obj.customer_email) + 'Phone: {}\n\n'.format(obj.phone) + \
              'Payment type: {}\n\n'.format(obj.payment_type)
    cart_items = get_cart(request)
    for element in cart_items:
        value = element['attributes'].sales_price \
            if element['attributes'].sales_price else element['attributes'].price
        value = convert(value)
        order_item = OrderItem(item=element['attributes'].item, quantity=element['quantity'],
                               size=element['attributes'].size, price=value, order=obj)
        order_item.save()
        size = 'size:' + str(element['attributes'].size) + ' - ' if element['attributes'].size else ''
        message += str(element['attributes'].item) + ' - ' + str(element['quantity']) \
                   + 'pcs' + ' - ' + size + str(value) + 'UAH' + '\n\n'
    message += 'Total cost - {}'.format(obj.total_cost)
    return message


class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'lions_heart_cart/order.html'

    def form_valid(self, form):
        cart = Cart(self.request)
        self.obj = form.save(commit=False)
        self.obj.total_cost = cart.get_total()
        self.obj.save()
        message = create_order_item(self.request, obj=self.obj)
        cart.clear()
        send_mail('Lions Heart', message, settings.EMAIL_HOST_USER,
                  [self.obj.customer_email, settings.STAFF_EMAIL])
        return HttpResponseRedirect(reverse('success'))
        # if self.obj.payment_type == 'Cash' or self.obj.payment_type == 'Наличные' or self.obj.payment_type == 'Готівка':
        #     return HttpResponseRedirect(reverse('success'))
        # else:
        #     data = liqpay(self.request, amount=self.obj.total_cost, order_id=self.obj.id)
        #
        #     try:
        #         del self.request.session['data']
        #     except KeyError:
        #         pass
        #
        #     self.request.session['data'] = data
        #
        #     return HttpResponseRedirect(reverse('pay'))

    def form_invalid(self, form):
        if 'phone' not in form.cleaned_data:
            messages.error(self.request,
                       _("Phone number must be entered in the format: '+380441234567'. Up to 12 digits allowed."))
        return HttpResponseRedirect(reverse('order'))

    def dispatch(self, request, *args, **kwargs):
        cart = Cart(self.request)
        if not cart.get_total():
            return redirect('home')
        return super(OrderCreate, self).dispatch(request, *args, **kwargs)


class PayView(TemplateView):
    template_name = 'lions_heart_cart/pay.html'

    def get_context_data(self, **kwargs):
        context = super(PayView, self).get_context_data(**kwargs)
        data = self.request.session['data']
        context['data'] = data
        return context


class SuccessView(TemplateView):
    template_name = 'lions_heart_cart/order_success.html'

