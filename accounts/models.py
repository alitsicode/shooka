from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Team_Member(models.Model):
    fullname=models.CharField(_("fullname"), max_length=100)
    company_role=models.CharField(_("company_role"), max_length=100)
    email=models.EmailField(_("email"), max_length=254)
    linkdin_id=models.CharField(_("linkdin_id"), max_length=100,null=True,blank=True)
    whatsapp_number=models.CharField(_("whatsapp_number"), max_length=10,null=True,blank=True)
    profile_photo=models.ImageField(_("profile_photo"), upload_to='member_profile/')
    created=models.DateTimeField(_("created"), auto_now_add=True)
    updated=models.DateTimeField(_("updated"), auto_now=True)


    class Meta:
        verbose_name = _("Team_Member")
        verbose_name_plural = _("Team_Members")

    def __str__(self):
        return self.fullname

