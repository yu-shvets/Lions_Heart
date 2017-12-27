from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Item
from django_filters.views import FilterView


class HomeView(TemplateView):
    template_name = 'lions_heart_products/index.html'


class ItemFilterView(FilterView):
    model = Item
    filter_fields = ['collection', 'category']
    template_name = 'lions_heart_products/catalogue.html'
    paginate_by = 7


class ItemDetailView(DetailView):
    model = Item
    template_name = 'lions_heart_products/item_detail.html'




# class CatalogueListView(ListView):
#     model = Item
#     template_name = 'lions_heart_products/catalogue.html'
#     context_object_name = 'products'
#     queryset = Item.objects.select_related(
#                     'category',
#                     'collection',
#             ).prefetch_related('image_set')
#
#
# class CollectionListView(CatalogueListView):
#     def get_queryset(self):
#         return self.queryset.filter(collection=self.kwargs['collection_id'])
#
#
# class CategoryListView(CatalogueListView):
#     def get_queryset(self):
#         return self.queryset.filter(category=self.kwargs['category_id'])