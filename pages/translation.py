from modeltranslation.translator import register, TranslationOptions
from .models import BlogCategory,NewCategory,Blog,New,Category,Product

@register(BlogCategory)
class BlogCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)
    
@register(NewCategory)
class NewCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title','text')

@register(New)
class NewTranslationOptions(TranslationOptions):
    fields = ('title','description')

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title','description')
