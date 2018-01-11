from lions_heart_products.models import Collection, Category


def project_variables(request):
    collections = Collection.objects.all()
    categories = Category.objects.all()
    return {'collections': collections, 'categories': categories}