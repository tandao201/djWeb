from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog.html")

def blog_details(request):
    return render(request, "blog-details.html")

def checkout(request):
    return render(request, "checkout.html")

def contact(request):
    return render(request, "contact.html")

def product_details(request):
    return render(request, "product-details.html")

def products(request):
    return render(request, "products.html")

def testimonials(request):
    return render(request, "testimonials.html")

