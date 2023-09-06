from django.contrib import admin
from .models import Blog,New,Category,Product,BlogCategory,NewCategory
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=['title','team_member','created']
    list_filter=['team_member','created']
    ordering=['-created']
    search_fields=['title']

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    list_display=['title']
    ordering=['-created']
    search_fields=['title']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title']
    ordering=['-created']
    search_fields=['title']

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display=['title']
    ordering=['-created']
    search_fields=['title']

@admin.register(NewCategory)
class NewCategoryAdmin(admin.ModelAdmin):
    list_display=['title']
    ordering=['-created']
    search_fields=['title']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['title']
    list_filter=['category']
    ordering=['-created']
    search_fields=['title']
