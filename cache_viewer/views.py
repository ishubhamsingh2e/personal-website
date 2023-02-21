from django.shortcuts import render, redirect
from django.core.cache import cache


def cache_viewer(request):
    cache_keys = cache.keys('*')
    cache_data = {}
    for key in cache_keys:
        cache_data[key] = cache.get(key)
    context = {
        'cache_data': cache_data
    }
    if 'delete_key' in request.GET:
        cache.delete(request.GET['delete_key'])
        return redirect('cache_viewer')
    return render(request, 'cache_viewer/view.html', context)
