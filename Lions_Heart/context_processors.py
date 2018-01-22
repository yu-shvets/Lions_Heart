from lions_heart_products.models import Collection, Category
from lions_heart_cart.cart import Cart
from lions_heart_products.currency_rates import rate

def project_variables(request):
    collections = Collection.objects.all()
    categories = Category.objects.order_by('-id')
    categories_first = categories[:4]
    categories_second = categories[4:]
    cart = Cart(request)
    items = len([i for i in cart])
    return {'collections': collections, 'categories': categories, 'categories_first': categories_first,
            'categories_second': categories_second, 'items': items, 'rate': rate}
