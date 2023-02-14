from .models import Blog
from django.contrib.sitemaps import Sitemap


class BlogSiteMap(Sitemap):
    changefreq = 'daily',
    priority = 0.9

    def items(self):
        return Blog.objects.all()

    def location(self, item):
        if item.slug is None:
            return '/blog/'
        return '/blog/' + item.slug

    def lastmod(self, obj):
        return obj.date
