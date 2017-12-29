from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Item
from django_filters.views import FilterView
import django_filters
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_filters.views import FilterView


class HomeView(TemplateView):
    template_name = 'lions_heart_products/index.html'


class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = ['collection', 'category']


def itemlistview(request):
    filtered = ItemFilter(
                      request.GET,
                      queryset=Item.objects.all()
                  )
    paginator = Paginator(filtered.qs, 7)

    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    return render(
        request,
        'lions_heart_products/catalogue.html',
        {'response': response, 'filter': filtered}
    )


class CollectionListView(FilterView):
    model = Item
    template_name = 'lions_heart_products/collection.html'
    filter_fields = ['category']
    paginate_by = 7

    def get_queryset(self):
        queryset = super(CollectionListView, self).get_queryset()
        return queryset.filter(collection=self.kwargs['collection_id'])


class ItemDetailView(DetailView):
    model = Item
    template_name = 'lions_heart_products/item_detail.html'




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