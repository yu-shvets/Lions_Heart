from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import Item, Category, Collection


class HomeView(TemplateView):
    template_name = 'lions_heart_products/index.html'


class CategoryListView(ListView):
    model = Item
    template_name = 'lions_heart_products/category.html'
    paginate_by = 8

    def get_queryset(self):
        queryset = super(CategoryListView, self).get_queryset()
        collection = Collection.objects.first()
        category_id = self.kwargs['category_id']
        if category_id == '7':
            return queryset.filter(category=self.kwargs['category_id'],
                                   collection=collection).order_by('-is_not_leather_chain', 'price')
        return queryset.filter(category=self.kwargs['category_id'], collection=collection).order_by('price')

    def get_paginate_by(self, queryset):
        return int(self.request.GET.get('paginate_by', self.paginate_by))

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['categs'] = get_object_or_404(Category, id=self.kwargs['category_id'])
        context['paginate_by'] = int(self.request.GET.get('paginate_by', self.paginate_by))
        return context


class CollectionListView(ListView):

    model = Item
    template_name = 'lions_heart_products/collection.html'
    paginate_by = 7

    def get_queryset(self):
        queryset = super(CollectionListView, self).get_queryset()
        collection_id = self.kwargs['collection_id']
        if collection_id == '2':
            return queryset.filter(collection=self.kwargs['collection_id']).order_by('created')
        return queryset.filter(collection=self.kwargs['collection_id']).order_by('price')

    def get_context_data(self, **kwargs):
        context = super(CollectionListView, self).get_context_data(**kwargs)
        context['collects'] = get_object_or_404(Collection, id=self.kwargs['collection_id'])
        return context


class CategoryCollectionListView(CollectionListView):

    def get_queryset(self):
        queryset = super(CategoryCollectionListView, self).get_queryset()
        category_id = self.kwargs['category_id']
        if category_id == '7':
            return queryset.filter(collection=self.kwargs['collection_id'],
                                   category=self.kwargs['category_id']).order_by('-is_not_leather_chain', 'price')
        return queryset.filter(collection=self.kwargs['collection_id'], category=self.kwargs['category_id'])

    def get_context_data(self, **kwargs):
        context = super(CategoryCollectionListView, self).get_context_data(**kwargs)
        context['categs'] = get_object_or_404(Category, id=self.kwargs['category_id'])
        return context


class SalesListView(ListView):
    model = Item
    template_name = 'lions_heart_products/sales.html'
    paginate_by = 8
    ordering = ['price']

    def get_queryset(self):
        queryset = super(SalesListView, self).get_queryset()
        return queryset.filter(sales__isnull=False)


class CollectionSalesListView(SalesListView):
    paginate_by = 7

    def get_queryset(self):
        queryset = super(CollectionSalesListView, self).get_queryset()
        return queryset.filter(sales__isnull=False, collection=self.kwargs['collection_id'])

    def get_context_data(self, **kwargs):
        context = super(CollectionSalesListView, self).get_context_data(**kwargs)
        context['selected'] = get_object_or_404(Collection, id=self.kwargs['collection_id'])
        return context


class ItemDetailView(DetailView):
    model = Item
    template_name = 'lions_heart_products/item_detail.html'

