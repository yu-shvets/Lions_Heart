from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Category, Item, Collection, Image


class HomeView(TemplateView):
    template_name = 'lions_heart_app/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['collections'] = Collection.objects.all()
        context['categories'] = Category.objects.all()
        return context


class CatalogueListView(ListView):
    model = Item
    template_name = 'lions_heart_app/catalogue.html'

    def get_queryset(self):
        queryset = super(CatalogueListView, self).get_queryset()

        if self.kwargs.get('category_id'):
            return queryset.filter(category=self.kwargs['category_id'])
        elif self.kwargs.get('collection_id'):
            return queryset.filter(collection=self.kwargs['collection_id'])
        else:
            return queryset

    def get_context_data(self, **kwargs):
        context = super(CatalogueListView, self).get_context_data(**kwargs)
        context['main_image'] = Image.objects.filter(main_image=True)
        return context


class ItemDetailView(DetailView):
    model = Item
    template_name = 'lions_heart_app/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        return context



