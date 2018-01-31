from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import Item, Category, Collection
import django_filters
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_filters.views import FilterView
# from .forms import SizesForm


class HomeView(TemplateView):
    template_name = 'lions_heart_products/index.html'




class CategoryListView(ListView):
    model = Item
    template_name = 'lions_heart_products/category.html'
    paginate_by = 1
    ordering = ['price']

    def get_queryset(self):
        queryset = super(CategoryListView, self).get_queryset()
        return queryset.filter(category=self.kwargs['category_id'])

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
    ordering = ['price']

    def get_queryset(self):
        queryset = super(CollectionListView, self).get_queryset()
        return queryset.filter(collection=self.kwargs['collection_id'])

    def get_context_data(self, **kwargs):
        context = super(CollectionListView, self).get_context_data(**kwargs)
        context['collects'] = get_object_or_404(Collection, id=self.kwargs['collection_id'])
        return context


class CategoryCollectionListView(CollectionListView):

    def get_queryset(self):
        queryset = super(CategoryCollectionListView, self).get_queryset()
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

    # def get_context_data(self, **kwargs):
    #     context = super(ItemDetailView, self).get_context_data(**kwargs)
    #     context['form'] = SizesForm(pk=self.kwargs.get('pk'))
    #     return context


# def choose_size(request, item_id):
#     item = get_object_or_404(Item, id=item_id)
#     form = SizesForm(pk=item_id)
#     if request.method == 'POST':
#         chosen_size = request.POST['size']
#         size = Sizes.objects.get(size=chosen_size, item=item)
#         print(size.price)
#         return render(request, 'lions_heart_products/item_detail_size.html', {'item': item, 'size': size, 'form': form})
#     else:
#         return HttpResponseRedirect('home')




# class ItemFilterView(FilterView):
#     model = Item
#     filter_fields = ['collection', 'category']
#     template_name = 'lions_heart_products/catalogue.html'
#     paginate_by = 1


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


# class ItemFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = Item
#         fields = ['collection', 'category']
#
#
# def itemlistview(request):
#     filtered = ItemFilter(
#                       request.GET,
#                       queryset=Item.objects.all()
#                   )
#     paginator = Paginator(filtered.qs, 7)
#
#     page = request.GET.get('page')
#     try:
#         response = paginator.page(page)
#     except PageNotAnInteger:
#         response = paginator.page(1)
#     except EmptyPage:
#         response = paginator.page(paginator.num_pages)
#
#     return render(
#         request,
#         'lions_heart_products/catalogue.html',
#         {'response': response, 'filter': filtered}
#     )


# class CollectionListView(FilterView):
#
#     model = Item
#     template_name = 'lions_heart_products/collection.html'
#     filter_fields = ['category']
#     paginate_by = 7
#
#     def get_queryset(self):
#         queryset = super(CollectionListView, self).get_queryset()
#         return queryset.filter(collection=self.kwargs['collection_id'])