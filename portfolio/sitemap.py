from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Project
from blog.models import Blog


class IndexSitemap(Sitemap):
    changefreq = "never"
    priority = 0.1

    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.1

    def items(self):
        return ['blog']

    def location(self, item):
        return reverse(item)


class RssSitemap(Sitemap):
    changefreq = "never"
    priority = 0.1

    def items(self):
        return ['rss']

    def location(self, item):
        return reverse(item)


class ProjectSitemap(Sitemap):
    changefreq = "always"
    priority = 0.9

    def items(self):
        return Project.objects.all()

    def location(self, obj):
        return reverse('project', args=[str(obj.id)])


class ArticleMap(Sitemap):
    changefreq = 'always'
    priority = 0.9

    def items(self):
        return Blog.objects.filter(status='published')

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.date
