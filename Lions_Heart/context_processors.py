from lions_heart_products.models import Collection, Category
from lions_heart_cart.cart import Cart

def project_variables(request):
    collections = Collection.objects.all()
    categories = Category.objects.all()
    categories_first = Category.objects.all()[:4]
    categories_second = Category.objects.all()[4:]
    cart = Cart(request)
    items = len([i for i in cart])
    return {'collections': collections, 'categories': categories,
            'categories_first': categories_first, 'categories_second': categories_second, 'items': items}
