from django.contrib import admin
from .models import *
import markdown


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('title', 'body')
    ordering = ('status', 'date')

    def save_model(self, request, obj, form, change):
        # Convert the Markdown to HTML
        obj.blog_html = markdown.markdown(obj.body,
                                          extensions=['tables', 'fenced_code',
                                                      'codehilite'])

        super().save_model(request, obj, form, change)


admin.site.register(Blog, BlogAdmin)