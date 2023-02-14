from django.shortcuts import render, get_object_or_404
from portfolio.models import AdminData
from .models import *
import random

from django.views.decorators.cache import cache_page


# Create your views here.

def blog(request):
    admin_data = AdminData.objects.first()
    _cat = AdminData.blog_category.all()
    blogs = Blog.objects.all().reverse()
    blogs_recent = blogs[:5]

    if request.method == "POST":
        searched = request.POST["query"]
        blogs = Blog.objects.filter(title__contains=searched)
        num_article = len(blogs)

        return render(request, 'blog/blog.html', {
            'admin_data': admin_data,
            'blogs': blogs,
            'recent': blogs_recent,
            'category': _cat,
            'length': num_article,
        })
    else:
        num_article = len(blogs)
        blogs_recent = blogs[:5]
        return render(request, 'blog/blog.html', {
            'admin_data': admin_data,
            'blogs': blogs,
            'recent': blogs_recent,
            'category': _cat,
            'length': num_article,
        })


def article(request, year, month, day, slug):
    _article = get_object_or_404(
        Blog,
        status='published',
        date=f"{year}-{month}-{day}",
        slug=slug
    )
    recommendation = Blog.objects.all().exclude(slug__exact=_article.slug)
    recommendation = random.choice(recommendation)
    return render(request, "blog/article.html", {
        'blog': _article,
        'recommendation': recommendation,
    })


def category(request, _filter):
    admin_data = AdminData.objects.first()
    blogs = Blog.objects.filter(cat=_filter.replace("-", " "))
    blogs_recent = Blog.objects.all()[0:5]
    _cat = AdminData.blog_category.all()
    num_article = len(blogs)

    return render(request, 'blog/blog.html', {
        'admin_data': admin_data,
        'blogs': blogs,
        'recent': blogs_recent,
        'category': _cat,
        'length': num_article,
    })
