from django.contrib import admin
from .models import Team_Member
# Register your models here.
@admin.register(Team_Member)
class Team_MemberAdmin(admin.ModelAdmin):
    list_display=['fullname','company_role','email']
    ordering=['-created']
    search_fields=['fullname']

