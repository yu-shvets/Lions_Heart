from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .cart import Cart
from lions_heart_app.models import Item
from django.shortcuts import get_object_or_404
from .models import Order, OrderItem
from django.forms import ModelForm
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView


def cart_view(request):
    cart = Cart(request)
    total_price = cart.get_total_price()
    return render(request, 'lions_heart_cart/cart.html', {'cart': cart, 'total_price': total_price})


def add_to_cart(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.add(item=item)
    return HttpResponseRedirect(reverse('catalogue'))


def cart_remove(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.remove(item)
    return HttpResponseRedirect(reverse('cart'))


class OrderView(TemplateView):
    template_name = 'lions_heart_cart/order.html'

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        context['form'] = OrderForm()
        return context


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ('customer_name', 'customer_email', 'phone', 'payment_type', 'comment')


class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'lions_heart_cart/order.html'

    def form_valid(self, form):
        cart = Cart(self.request)

        self.obj = form.save(commit=False)
        self.obj.total_cost = cart.get_total_price()
        self.obj.save()

        for element in cart:
            order_item = OrderItem(item=element['item'], quantity=element['quantity'],
                                   price=float(element['price']), order=self.obj)
            order_item.save()
        cart.clear()
        return HttpResponseRedirect(reverse('catalogue'))

    def get_success_url(self):
            return reverse('home')



