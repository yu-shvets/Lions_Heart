from lions_heart_products.models import Collection, Category
from lions_heart_cart.cart import Cart
from lions_heart_products.templatetags.mytemplatetags import get_rate
from lions_heart_blog.models import CompanyInformation


def project_variables(request):
    collections = Collection.objects.all()
    lions_heart = Collection.objects.get(id=1)
    revived = Collection.objects.get(id=2)
    categories = Category.objects.order_by('-id')
    categories_first = categories[:5]
    categories_second = categories[5:]
    cart = Cart(request)
    items = cart.cart_len()
    rate = get_rate()
    company_info = CompanyInformation.objects.first()
    page_items = [7, 14, 28, 56]
    return {'collections': collections, 'categories': categories, 'categories_first': categories_first,
            'categories_second': categories_second, 'items': items, 'rate': rate, 'company_info': company_info,
            'lions_heart': lions_heart, 'revived': revived, 'page_items': page_items}
