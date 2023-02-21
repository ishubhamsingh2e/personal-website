from django.urls import path
from .views import cache_viewer

app_name = 'cache_viewer'

urlpatterns = [
    path('', cache_viewer, name='cache_viewer'),
]
