from django.contrib import admin
from lions_heart_products.models import Category, Item, Image, Collection, Specs, CurrencyRate, Attributes

admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Collection)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


class SpecsInline(admin.StackedInline):
    model = Specs
    extra = 0


class AttributesInline(admin.TabularInline):
    model = Attributes
    extra = 0


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = (AttributesInline, ImageInline, SpecsInline)
    ordering = ['collection', 'category', 'title']


@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    pass