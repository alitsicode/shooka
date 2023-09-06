from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.
class AboutUs(models.Model):
    company_name=models.CharField(_("company_name"), max_length=50)
    logo=models.ImageField(_("logo"), upload_to='logo/')
    description=RichTextField()
    address=RichTextField()
    phone_number=models.CharField(_("phone_number"), max_length=11)
    email=models.EmailField(_("email"), max_length=254)
    linkdin_id=models.CharField(_("linkdin_id"), max_length=40,null=True,blank=True)
    instagram_id=models.CharField(_("instagram_id"), max_length=40,null=True,blank=True)
    whatsapp_number=models.CharField(_("whatsapp_number"), max_length=10,null=True,blank=True)
    telegram_id=models.CharField(_("telegram_id"), max_length=40,null=True,blank=True)
    eita_id=models.CharField(_("eita_id"), max_length=40,null=True,blank=True)
    created=models.DateTimeField(_("created"), auto_now_add=True)
    updated=models.DateTimeField(_("updated"), auto_now=True)
    

    class Meta:
        verbose_name = _("AboutUs")
        verbose_name_plural = _("AboutUs")

    def __str__(self):
        return self.company_name

class ContactUs(models.Model):
    fullname=models.CharField(_("fullname"), max_length=100)
    email=models.EmailField(_("email"), max_length=254)
    text=models.TextField(_("text"))
    show_as_client_think=models.BooleanField(_("show_as_client_think"),default=False)
    created=models.DateTimeField(_("created"), auto_now_add=True)
    

    class Meta:
        verbose_name = _("ContactUs")
        verbose_name_plural = _("ContactUs")

    def __str__(self):
        return self.fullname

class Why_Choose_Us(models.Model):
    title=models.CharField(_("title"), max_length=100)
    created=models.DateTimeField(_("created"), auto_now_add=True)
    updated=models.DateTimeField(_("updated"), auto_now=True)
    

    class Meta:
        verbose_name = _("Why_Choose_Us")
        verbose_name_plural = _("Why_Choose_Us")

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question=models.CharField(_("question"), max_length=100)
    answer=RichTextField()
    created=models.DateTimeField(_("created"), auto_now_add=True)
    updated=models.DateTimeField(_("updated"), auto_now=True)
    

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")

    def __str__(self):
        return self.question

class Company_Work_Together(models.Model):
    company_name=models.CharField(_("company_name"), max_length=100)
    company_logo=models.ImageField(_("company_logo"), upload_to='other_companies_logo/')
    created=models.DateTimeField(_("created"), auto_now_add=True)
    updated=models.DateTimeField(_("updated"), auto_now=True)
    

    class Meta:
        verbose_name = _("Company_Work_Together")
        verbose_name_plural = _("Companies_Work_Together")

    def __str__(self):
        return self.company_name


