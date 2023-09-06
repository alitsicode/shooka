from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('products/',views.ProductListView.as_view(),name='products'),
    path('product_detail/<int:pk>',views.ProductDetailView.as_view(),name='product_detail'),
    path('product_category/<int:pk>',views.ProductOfCategoryListView.as_view(),name='product_category'),
    path('blog_category/<int:pk>',views.BlogOfCategoryListView.as_view(),name='blog_category'),
    path('new_category/<int:pk>',views.NewOfCategoryListView.as_view(),name='new_category'),
    path('news/',views.NewsListView.as_view(),name='news'),
    path('news_detail/<int:pk>',views.NewsDetailView.as_view(),name='news_detail'),
    path('blogs/',views.BlogsListView.as_view(),name='blogs'),
    path('blogs_detail/<int:pk>',views.BlogsDetailView.as_view(),name='blogs_detail'),
    path('search_product/',views.search_product.as_view(),name='search_product'),
    path('search_new/',views.search_new.as_view(),name='search_new'),
    path('search_blog/',views.search_blog.as_view(),name='search_blog'),
]
