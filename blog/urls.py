from django.urls import path
from .feed import BlogsFeed
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path(
        '<slug:slug>/',
        views.article,
        name='article'
    ),
    path('rss/', BlogsFeed(), name='rss'),
    path('category/<_filter>/', views.category, name='category'),
]
