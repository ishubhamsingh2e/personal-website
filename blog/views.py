from django.shortcuts import render, get_object_or_404
from portfolio.models import AdminData
from .models import *
import random

from django.views.decorators.cache import cache_page
from django.core.cache import cache


# Create your views here.

@cache_page(60*15)
def blog(request):
    admin_data = cache.get("admin-data")
    if not admin_data:
        admin_data = AdminData.objects.first()
        admin_data = cache.set("admin-data", admin_data, timeout=60 * 1440 * 30)

    _cat = cache.get("cat")
    if not _cat:
        _cat = AdminData.blog_category.all()
        cache.set("cat", _cat, timeout=60 * 1440 * 30)

    blogs = cache.get("blogs")
    if not blogs:
        blogs = Blog.objects.all().reverse()
        cache.set("blogs", blogs, timeout=60 * 1440 * 30)
    blogs_recent = blogs.reverse()[:5]

    # TODO fix search error
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


@cache_page(60 * 15)
def article(request, year, month, day, slug):
    _article = cache.get(f"{slug}")
    if not _article:
        _article = get_object_or_404(
            Blog,
            status='published',
            date=f"{year}-{month}-{day}",
            slug=slug
        )
        cache.set(f"{slug}", _article, timeout=60 * 1440 * 30)

    _blog = cache.get("blog-all")
    if not _blog:
        _blog = Blog.objects.all()
        cache.set("blog-all", _blog, timeout=60 * 1440 * 30)

    recommendation = _blog.exclude(slug__exact=_article.slug)
    recommendation = random.choice(recommendation)
    return render(request, "blog/article.html", {
        'blog': _article,
        'recommendation': recommendation,
    })


@cache_page(60 * 15)
def category(request, _filter):
    admin_data = cache.get("admin-data")
    if not admin_data:
        admin_data = AdminData.objects.first()
        cache.set("admin-data", admin_data, timeout=60 * 1440 * 30)

    blogs = Blog.objects.filter(cat=_filter.replace("-", " "))

    _blog = cache.get("blog-all")
    if not _blog:
        _blog = Blog.objects.all()
        cache.set("blog-all", _blog, timeout=60 * 1440 * 30)
    blogs_recent = _blog[0:5]

    _cat = AdminData.blog_category.all()
    num_article = len(blogs)

    return render(request, 'blog/blog.html', {
        'admin_data': admin_data,
        'blogs': blogs,
        'recent': blogs_recent,
        'category': _cat,
        'length': num_article,
    })
