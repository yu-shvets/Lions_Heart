from django.contrib import admin
from lions_heart_products.models import Category, Item, Image, Collection, Specs

admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Collection)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


class SpecsInline(admin.TabularInline):
    model = Specs


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = (ImageInline, SpecsInline)

