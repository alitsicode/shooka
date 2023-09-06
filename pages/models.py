from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import Team_Member
from django.utils.translation import gettext_lazy as _
# Create your models here.

class BlogCategory(models.Model):
    title=models.CharField(_("title"), max_length=50)
    image=models.ImageField(_("image"), upload_to='category_image/')
    created=models.DateTimeField(_("created"), auto_now_add=True)
    updated=models.DateTimeField(_("updated"), auto_now=True)
    

    class Meta:
        verbose_name = _("BlogCategory")
        verbose_name_plural = _("BlogCategories")

    def __str__(self):
        return self.title

class NewCategory(models.Model):
    title=models.CharField(_("title"), max_length=50)
    image=models.ImageField(_("image"), upload_to='category_image/')
    created=models.DateTimeField(_("created"), auto_now_add=True)
    updated=models.DateTimeField(_("updated"), auto_now=True)
    

    class Meta:
        verbose_name = _("NewCategory")
        verbose_name_plural = _("NewCategories")

    def __str__(self):
        return self.title



class Blog(models.Model):
    title=models.CharField(_("title"), max_length=100)
    text=RichTextField()
    category=models.ManyToManyField(BlogCategory, verbose_name=_("category"),related_name='blog')
    image=models.ImageField(_("image"), upload_to='blog_image/')
    team_member=models.ForeignKey(Team_Member, verbose_name=_("team_member"), on_delete=models.CASCADE)
    is_publish=models.BooleanField(_("is_publish"),default=False)
    created=models.DateTimeField(_("created"), auto_now_add=True)
    updated=models.DateTimeField(_("updated"), auto_now=True)
    

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")

    def __str__(self):
        return self.title

class New(models.Model):
    title=models.CharField(_("title"), max_length=150)
    description=RichTextField()
    category=models.ManyToManyField(NewCategory, verbose_name=_("category"),related_name='new')
    image=models.ImageField(_("image"), upload_to='news_image/')
    is_publish=models.BooleanField(_("is_publish"),default=False)
    created=models.DateTimeField(_("created"), auto_now_add=True)
    updated=models.DateTimeField(_("updated"), auto_now=True)
    

    class Meta:
        verbose_name = _("New")
        verbose_name_plural = _("News")

    def __str__(self):
        return self.title

class Category(models.Model):
    title=models.CharField(_("title"), max_length=50)
    image=models.ImageField(_("image"), upload_to='category_image/')
    created=models.DateTimeField(_("created"), auto_now_add=True)
    updated=models.DateTimeField(_("updated"), auto_now=True)
    

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title

class Product(models.Model):
    title=models.CharField(_("title"), max_length=100)
    description=RichTextField()
    image=models.ImageField(_("image"), upload_to='product_image/')
    category=models.ManyToManyField(Category, verbose_name=_("category"),related_name='product')
    created=models.DateTimeField(_("created"), auto_now_add=True)
    updated=models.DateTimeField(_("updated"), auto_now=True)
    

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.title

