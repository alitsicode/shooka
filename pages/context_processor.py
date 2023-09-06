from .models import Category,BlogCategory,NewCategory

def category(request):
    product_category=Category.objects.all()
    return {'product_category':product_category}

def news_category(request):
    news_category=NewCategory.objects.all()
    return {'news_category':news_category}

def blogs_category(request):
    blogs_category=BlogCategory.objects.all()
    return {'blogs_category':blogs_category}