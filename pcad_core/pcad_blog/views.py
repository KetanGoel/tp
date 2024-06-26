from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def blog(request):
    return render(request, "blogindex.html")

from .models import BlogDetails

def blog_page(request):
    blogs = BlogDetails.objects.all().order_by('-upload_date')
    for blog in blogs:
        print(blog.title, blog.upload_date)  
    return render(request, 'blogindex.html', {'blogs': blogs})
