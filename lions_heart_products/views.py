from django.views.generic import TemplateView, ListView, DetailView
from .models import Item


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

    def get_queryset(self):
        if self.kwargs.get('category_id'):
            return self.queryset.filter(category=self.kwargs['category_id']).order_by('category')
        elif self.kwargs.get('collection_id'):
            return self.queryset.filter(collection=self.kwargs['collection_id'])
        else:
            return Item.objects.all()


class WomenLisView(CatalogueListView):
    def get_queryset(self):
        return self.queryset.filter(collection=self.kwargs['collection_id'], type='Женская')


class MenListView(CatalogueListView):
    def get_queryset(self):
        return self.queryset.filter(collection=self.kwargs['collection_id'], type='Мужская')


class ItemDetailView(DetailView):
    model = Item
    template_name = 'lions_heart_products/item_detail.html'



