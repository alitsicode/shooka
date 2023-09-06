from modeltranslation.translator import register, TranslationOptions
from .models import Team_Member

@register(Team_Member)
class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('fullname', 'company_role',)