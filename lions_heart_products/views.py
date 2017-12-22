from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Item, Collection
import django_filters


class HomeView(TemplateView):
    template_name = 'lions_heart_products/index.html'


class CatalogueListView(ListView):
    model = Item
    template_name = 'lions_heart_products/catalogue.html'
    context_object_name = 'products'
    queryset = Item.objects.select_related(
                    'category',
                    'collection',
            ).prefetch_related('image_set')


class CollectionListView(CatalogueListView):
    def get_queryset(self):
        return self.queryset.filter(collection=self.kwargs['collection_id'])


class CategoryListView(CatalogueListView):
    def get_queryset(self):
        return self.queryset.filter(category=self.kwargs['category_id'])


class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'lions_heart_products/collection_detail.html'


def collection_category(request, collection_id, category_id):
    items = Item.objects.filter(collection=collection_id, category=category_id )
    return render(request, 'lions_heart_products/catalogue.html', {'products': items})


def women_collection(request, collection_id):
    items = Item.objects.filter(collection=collection_id, type='Женская')
    return render(request, 'lions_heart_products/catalogue.html', {'products': items})


def men_collection(request, collection_id):
    items = Item.objects.filter(collection=collection_id, type='Мужская')
    return render(request, 'lions_heart_products/catalogue.html', {'products': items})


class ItemDetailView(DetailView):
    model = Item
    template_name = 'lions_heart_products/item_detail.html'


class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = ['type', 'collection', 'category']


def product_list(request):
    filter = ItemFilter(request.GET, queryset=Item.objects.all())
    return render(request, 'lions_heart_products/catalogue.html', {'filter': filter})
