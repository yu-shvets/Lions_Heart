from django.shortcuts import render, reverse, HttpResponseRedirect
from .cart import Cart
from lions_heart_products.models import Item
from django.shortcuts import get_object_or_404
from .models import Order, OrderItem
from .forms import CartAddProductForm, OrderForm
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.core.exceptions import ValidationError
from django.http import JsonResponse


def cart_view(request):
    cart = Cart(request)
    total_price = cart.get_total_price()
    form = CartAddProductForm()
    return render(request, 'lions_heart_cart/cart.html', {'cart': cart, 'total_price': total_price, 'form': form})


def add_to_cart(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.add(item=item)
    return HttpResponseRedirect(reverse('cart'))


def cart_remove(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.remove(item)
    return HttpResponseRedirect(reverse('cart'))


def update_quantity(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    form = CartAddProductForm(data=request.POST)
    response_data = {}
    if form.is_valid():
        data = form.cleaned_data
        new_quantity = data['quantity']
        cart.update(item, new_quantity)
        response_data['quantity'] = new_quantity
        response_data['sum'] = new_quantity * item.price
        response_data['total_price'] = cart.get_total_price()
    return JsonResponse(response_data)


class OrderView(TemplateView):
    template_name = 'lions_heart_cart/order.html'

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        context['form'] = OrderForm()
        return context


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
        return HttpResponseRedirect(reverse('home'))




