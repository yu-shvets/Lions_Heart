from modeltranslation.translator import register, TranslationOptions
from lions_heart_blog.models import Post, CompanyInformation


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'body_text',)


@register(CompanyInformation)
class CompanyInformationTranslationOptions(TranslationOptions):
    fields = ('about', 'address',)
