from modeltranslation.translator import register, TranslationOptions
from lions_heart_products.models import Collection, Category, Item, Specs


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Collection)
class CollectionTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Item)
class ItemTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Specs)
class SpecsTranslationOptions(TranslationOptions):
    fields = ('specs',)
