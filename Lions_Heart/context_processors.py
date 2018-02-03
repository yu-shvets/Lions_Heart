from lions_heart_products.models import Collection, Category
from lions_heart_cart.cart import Cart
from lions_heart_products.templatetags.mytemplatetags import get_rate
from lions_heart_blog.models import CompanyInformation

def project_variables(request):
    collections = Collection.objects.all()
    categories = Category.objects.order_by('-id')
    categories_first = categories[:4]
    categories_second = categories[4:]
    cart = Cart(request)
    items = cart.cart_len()
    rate = get_rate()
    company_info = CompanyInformation.objects.first()
    return {'collections': collections, 'categories': categories, 'categories_first': categories_first,
            'categories_second': categories_second, 'items': items, 'rate': rate, 'company_info': company_info}
