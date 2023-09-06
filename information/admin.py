from django.contrib import admin
from .models import ContactUs,AboutUs,Why_Choose_Us,FAQ,Company_Work_Together
# Register your models here.

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display=['company_name','phone_number','email','linkdin_id']
    ordering=['-created']

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display=['fullname','email','show_as_client_think','created']
    ordering=['-created']
    search_fields=['fullname']
   
@admin.register(Why_Choose_Us)
class Why_Choose_UsAdmin(admin.ModelAdmin):
    list_display=['title']
    ordering=['-created']
    search_fields=['title']

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display=['question']
    ordering=['-created']
    search_fields=['question']

@admin.register(Company_Work_Together)
class Company_Work_TogetherAdmin(admin.ModelAdmin):
    list_display=['company_name']
    ordering=['-created']
    search_fields=['company_name']
