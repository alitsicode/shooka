from modeltranslation.translator import register, TranslationOptions
from .models import AboutUs,Why_Choose_Us,FAQ

@register(AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('company_name', 'description','address')

@register(Why_Choose_Us)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(FAQ)
class FAQTranslationOptions(TranslationOptions):
    fields = ('question','answer')