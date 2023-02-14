from django.urls import path
from .feed import BlogsFeed
from django.contrib.sitemaps.views import sitemap
from .sitemap import BlogSiteMap
from . import views

sitemaps = {'blog': BlogSiteMap, }

urlpatterns = [
    path('', views.blog, name='blog'),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:slug>/',
        views.article,
        name='article'
    ),
    path('rss/', BlogsFeed(), name='rss'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('category/<_filter>/', views.category, name='category'),
]
