from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from .models import Blog


class BlogsFeed(Feed):
    title = "ishubhamsingh blog"
    link = reverse_lazy("blog")
    description = "latest post on ishubhamsingh blog"

    def items(self):
        return Blog.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_link(self, item):
        return '/blog/{}'.format(item.slug)
