from django.urls import path
from . import views
urlpatterns = [
    path('about/', views.about, name='about' ),
    path('blog-details/', views.blog_details, name='blog-details' ),
    path('blog/', views.blog, name='blog' ),
    path('checkout/', views.checkout, name='checkout' ),
    path('contact/', views.contact, name='contact' ),
    path('', views.index, name='index' ),
    path('product-details/', views.product_details, name='product-details' ),
    path('products/', views.products, name='products' ),
    path('testimonials/', views.testimonials, name='testimonials' ),
]   