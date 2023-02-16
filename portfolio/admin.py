from django.contrib import admin
from django.core.cache import cache

from .models import *


class DataAdmin(admin.ModelAdmin):
    list_display = ('userName', 'email', 'blog_category')

    def save_model(self, request, obj, form, change):
        if cache.get("admin-data"):
            cache.delete("admin-data")

        super().save_model(request, obj, form, change)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'project_url')

    def save_model(self, request, obj, form, change):
        if cache.get(f"project-{obj.id}"):
            cache.delete(f"project-{obj.id}")

        super().save_model(request, obj, form, change)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('field', 'title')

    def save_model(self, request, obj, form, change):
        if cache.get("services"):
            cache.delete("services")

        super().save_model(request, obj, form, change)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill', 'level')

    def save_model(self, request, obj, form, change):
        if cache.get("skills"):
            cache.delete("skills")

        super().save_model(request, obj, form, change)


class StoryEducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'syear', 'eyear')

    def save_model(self, request, obj, form, change):
        if cache.get("education"):
            cache.delete("education")

        super().save_model(request, obj, form, change)


class StoryExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'syear', 'eyear')

    def save_model(self, request, obj, form, change):
        if cache.get("experience"):
            cache.delete("experience")

        super().save_model(request, obj, form, change)


admin.site.register(AdminData, DataAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(StoryEducation, StoryEducationAdmin)
admin.site.register(StoryExperience, StoryExperienceAdmin)
admin.site.register(Project, ProjectAdmin)
