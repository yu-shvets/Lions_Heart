from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import Item, Category, Collection


class HomeView(TemplateView):
    template_name = 'lions_heart_products/index.html'


class CategoryListView(ListView):
    model = Item
    template_name ='lions_heart_products/category.html'
    paginate_by = 8

    def get_queryset(self):
        queryset = super(CategoryListView, self).get_queryset()
        category_id = self.kwargs['category_id']
        if category_id == '7':
            return queryset.filter(category=self.kwargs['category_id']).order_by('-is_leather_bracelet', 'price')
        return queryset.filter(category=self.kwargs['category_id']).order_by('price')

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['categs'] = get_object_or_404(Category, id=self.kwargs['category_id'])
        return context


class CollectionCategoryListView(CategoryListView):
    paginate_by = 7

    def get_queryset(self):
        queryset = super(CollectionCategoryListView, self).get_queryset()
        return queryset.filter(category=self.kwargs['category_id'], collection=self.kwargs['collection_id'])

    def get_context_data(self, **kwargs):
        context = super(CollectionCategoryListView, self).get_context_data(**kwargs)
        context['selected'] = get_object_or_404(Collection, id=self.kwargs['collection_id'])
        return context


class CollectionListView(ListView):

    model = Item
    template_name = 'lions_heart_products/collection.html'
    paginate_by = 7

    def get_queryset(self):
        queryset = super(CollectionListView, self).get_queryset()
        collection_id = self.kwargs['collection_id']
        if collection_id == '2':
            return queryset.filter(collection=self.kwargs['collection_id']).order_by('-created')
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
                                   category=self.kwargs['category_id']).order_by('-is_leather_bracelet', 'price')
        return queryset.filter(collection=self.kwargs['collection_id'], category=self.kwargs['category_id'])

    def get_context_data(self, **kwargs):
        context = super(CategoryCollectionListView, self).get_context_data(**kwargs)
        context['categs'] = get_object_or_404(Category, id=self.kwargs['category_id'])
        return context


class SalesCollectionListView(CollectionListView):

    def get_queryset(self):
        queryset = super(SalesCollectionListView, self).get_queryset()
        return queryset.filter(collection=self.kwargs['collection_id'], sales__isnull=False)

    def get_context_data(self, **kwargs):
        context = super(SalesCollectionListView, self).get_context_data(**kwargs)
        context['sales'] = True
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


class UniqueGiftsListView(ListView):
    model = Item
    template_name = 'lions_heart_products/gifts.html'
    paginate_by = 8
    ordering = ['price']

    def get_queryset(self):
        queryset = super(UniqueGiftsListView, self).get_queryset()
        return queryset.filter(unique_gift=True)


class CollectionUniqueGiftsListView(UniqueGiftsListView):
    paginate_by = 7

    def get_queryset(self):
        queryset = super(CollectionUniqueGiftsListView, self).get_queryset()
        return queryset.filter(unique_gift=True, collection=self.kwargs['collection_id'])

    def get_context_data(self, **kwargs):
        context = super(CollectionUniqueGiftsListView, self).get_context_data(**kwargs)
        context['selected'] = get_object_or_404(Collection, id=self.kwargs['collection_id'])
        return context


class ItemDetailView(DetailView):
    model = Item
    template_name = 'lions_heart_products/item_detail.html'

