from lions_heart_products.models import Collection, Category
from lions_heart_blog.models import CompanyInformation


def project_variables(request):
    collections = Collection.objects.all()
    categories = Category.objects.all()
    info = CompanyInformation.objects.first()
    return {'collections': collections, 'categories': categories, 'info': info}