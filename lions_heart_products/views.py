from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.views.generic import TemplateView, ListView, DetailView
from .models import Item, Category, Collection, Attributes, Specs
from .forms import AttributesForm
from django.http import JsonResponse
from lions_heart_products.templatetags.mytemplatetags import get_rate
from decimal import Decimal


class HomeView(TemplateView):
    template_name = 'lions_heart_products/index.html'


class CollectionListView(ListView):
    model = Item
    template_name = 'lions_heart_products/collection.html'
    paginate_by = 7

    def get_queryset(self):
        queryset = super(CollectionListView, self).get_queryset()
        collection_id = self.kwargs['collection_id']
        if collection_id == '2':
            return queryset.filter(collection=self.kwargs['collection_id']).order_by('created')
        return queryset.filter(collection=self.kwargs['collection_id']).order_by('position')

    def get_context_data(self, **kwargs):
        context = super(CollectionListView, self).get_context_data(**kwargs)
        context['collects'] = get_object_or_404(Collection, id=self.kwargs['collection_id'])
        context['paginate_by'] = int(self.request.GET.get('paginate_by', self.paginate_by))
        return context

    def get_paginate_by(self, queryset):
        return int(self.request.GET.get('paginate_by', self.paginate_by))


class CategoryCollectionListView(CollectionListView):

    def get_queryset(self):
        queryset = super(CategoryCollectionListView, self).get_queryset()
        category_id = self.kwargs['category_id']
        if category_id == '7':
            return queryset.filter(collection=self.kwargs['collection_id'],
                            category=self.kwargs['category_id']).order_by('-is_not_leather_chain', 'position')
        return queryset.filter(collection=self.kwargs['collection_id'], category=self.kwargs['category_id'])

    def get_context_data(self, **kwargs):
        context = super(CategoryCollectionListView, self).get_context_data(**kwargs)
        context['categs'] = get_object_or_404(Category, id=self.kwargs['category_id'])
        return context


class SalesListView(ListView):
    model = Item
    template_name = 'lions_heart_products/sales.html'
    paginate_by = 8
    ordering = ['position']

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

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['form'] = AttributesForm(pk=self.kwargs.get('pk'))
        return context


def update_size(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    response_data = {}
    rate = get_rate()
    if request.method == 'POST':
        chosen_size = request.POST['size']
        attributes = Attributes.objects.filter(size=chosen_size, item=item).first()
        response_data['price'] = Decimal(round(float(attributes.price) * rate)).quantize(Decimal('.00'))
        if attributes.sales_price:
            response_data['sales_price'] = Decimal(round(float(attributes.sales_price) * rate)).quantize(Decimal('.00'))
        response_data['weight'] = str(attributes.weight)
        response_data['diameter'] = str(attributes.diameter)
        response_data['width'] = str(attributes.width)
        response_data['height'] = str(attributes.height)
        response_data['length'] = str(attributes.length)
        response_data['size_id'] = attributes.id
    return JsonResponse(response_data)
