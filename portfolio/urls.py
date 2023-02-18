from django.urls import path
from . import views

from django.contrib.sitemaps.views import sitemap
from .sitemap import *

sitemaps = {
    'index': IndexSitemap,
    'project': ProjectSitemap,
    'blog': BlogSitemap,
    'rss': RssSitemap,
    'articles': ArticleMap
}

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<project_id>', views.project, name='project'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]
