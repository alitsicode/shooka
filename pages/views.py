from django.shortcuts import render,get_object_or_404
from information.models import Why_Choose_Us,Company_Work_Together,ContactUs
from .models import Blog,New,Product,Category,BlogCategory,NewCategory
from django.views import generic
from accounts.models import Team_Member
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.
def home(request):
    products=Product.objects.order_by('-created')[:4]
    news=New.objects.filter(is_publish=True).order_by('-created')[:3]
    blogs=Blog.objects.filter(is_publish=True).order_by('-created')[:3]
    contacts=ContactUs.objects.filter(show_as_client_think=True)
    companies=Company_Work_Together.objects.all()
    team_members=Team_Member.objects.all()
    why_us=Why_Choose_Us.objects.order_by('-created')[:4]
    return render(request,'pages/home.html',context={'why_us':why_us,'team_members':team_members,'companies':companies,'contacts':contacts,'blogs':blogs,'news':news,'products':products})

class ProductListView(generic.ListView):
    model = Product
    template_name = "pages/products.html"
    paginate_by=6
    context_object_name='products'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] =Category.objects.all() 
        return context

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "pages/product_detail.html"
    context_object_name='product'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] =Category.objects.all() 
        return context
    
class ProductOfCategoryListView(generic.ListView):
    template_name='pages/products_category.html'
    model=Category
    def get_context_data(self, **kwargs):
        pk=self.kwargs['pk']
        categorie=get_object_or_404(Category,pk=pk)
        product_category=categorie.product.all()
        paginated = Paginator(product_category, 6)
        page_number = self.request.GET.get('page') #Get the requested page number from the URL
        page = paginated.get_page(page_number)
        context = super().get_context_data(**kwargs)
        context["page_obj"] = page
        context["categories"] =Category.objects.all()
        context["current"] =categorie
        return context


class NewsListView(generic.ListView):
    model = New
    template_name = "pages/news.html"
    paginate_by=6
    context_object_name='news'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] =NewCategory.objects.all() 
        return context

class NewsDetailView(generic.DetailView):
    model = New
    template_name = "pages/new_detail.html"
    context_object_name='new'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] =NewCategory.objects.all() 
        return context


class NewOfCategoryListView(generic.ListView):
    template_name='pages/new_category.html'
    model=NewCategory
    def get_context_data(self, **kwargs):
        pk=self.kwargs['pk']
        categorie=get_object_or_404(NewCategory,pk=pk)
        new_category=categorie.new.all()
        paginated = Paginator(new_category, 6)
        page_number = self.request.GET.get('page') #Get the requested page number from the URL
        page = paginated.get_page(page_number)
        context = super().get_context_data(**kwargs)
        context["page_obj"] = page
        context["categories"] =NewCategory.objects.all()
        context["current"] =categorie
        return context


class BlogsListView(generic.ListView):
    model = Blog
    template_name = "pages/blogs.html"
    paginate_by=6
    context_object_name='blogs'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] =BlogCategory.objects.all() 
        return context

class BlogsDetailView(generic.DetailView):
    model = Blog
    template_name = "pages/blog_detail.html"
    context_object_name='blog'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] =BlogCategory.objects.all() 
        return context


class BlogOfCategoryListView(generic.ListView):
    template_name='pages/blog_category.html'
    model=BlogCategory
    def get_context_data(self, **kwargs):
        pk=self.kwargs['pk']
        categorie=get_object_or_404(BlogCategory,pk=pk)
        new_category=categorie.blog.all()
        paginated = Paginator(new_category, 6)
        page_number = self.request.GET.get('page') #Get the requested page number from the URL
        page = paginated.get_page(page_number)
        context = super().get_context_data(**kwargs)
        context["page_obj"] = page
        context["categories"] =BlogCategory.objects.all()
        context["current"] =categorie
        return context

class search_product(generic.ListView):
    template_name='pages/products.html'
    model=Product
    context_object_name='products'
    paginate_by=6
    def get_queryset(self):
        query=self.request.GET.get("search")
        products = Product.objects.all().filter(Q(title__icontains=query)) 
        return products
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] =Category.objects.all() 
        return context

class search_blog(generic.ListView):
    template_name='pages/blogs.html'
    model=Product
    context_object_name='blogs'
    paginate_by=6
    def get_queryset(self):
        query=self.request.GET.get("search")
        blogs = Blog.objects.all().filter(Q(title__icontains=query)) 
        return blogs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] =BlogCategory.objects.all() 
        return context

class search_new(generic.ListView):
    template_name='pages/news.html'
    model=Product
    context_object_name='news'
    paginate_by=6
    def get_queryset(self):
        query=self.request.GET.get("search")
        news = New.objects.all().filter(Q(title__icontains=query)) 
        return news

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] =NewCategory.objects.all() 
        return context