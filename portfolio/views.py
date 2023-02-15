from django.shortcuts import render

from blog.models import Blog
from .models import *

from django.views.decorators.cache import cache_page
from django.core.cache import cache

# Create your views here.


@cache_page(60 * 15)
def index(request):
    services = cache.get("services")
    if not services:
        services = Service.objects.all()
        cache.set("services", services, timeout=60 * 1440 * 30)

    skills = cache.get("skills")
    if not skills:
        skills = Skill.objects.all()
        cache.set("services", skills, timeout=60 * 1440 * 30)

    admin_data = cache.get("admin-data")
    if not admin_data:
        admin_data = AdminData.objects.first()
        cache.set("admin-data", admin_data, timeout=60 * 1440 * 30)

    education = cache.get("education")
    if not education:
        education = StoryEducation.objects.all().order_by("id").reverse()
        cache.set("education", education, timeout=60 * 1440 * 30)

    experience = cache.get("experience")
    if not experience:
        experience = StoryExperience.objects.all().order_by("id").reverse()
        cache.set("experience", experience, timeout=60 * 1440 * 30)

    _project = cache.get("project-all")
    if not _project:
        _project = Project.objects.all()
        cache.set("project-all", _project, timeout=60 * 1440 * 30)

    _blog = cache.get("blog-all")
    if not _blog:
        _blog = Blog.objects.all()
        cache.set("blog-all", _blog, timeout=60 * 1440 * 30)
    _blog = _blog[:3]

    education_last = len(education)
    experience_last = len(experience)

    skill = []
    for i in range(0, len(skills), 2):
        skill.append(skills[i:i + 2])

    return render(request, 'portfolio/index.html', {
        'services': services,
        'skills': skill,
        'admin_data': admin_data,
        'education': education,
        'lenEducation': education_last,
        'experience': experience,
        'lenExperience': experience_last,
        'projects': _project,
        'blogs': _blog,
    })


@cache_page(60 * 15)
def project(request, project_id):
    admin_data = cache.get("admin-data")
    if not admin_data:
        admin_data = AdminData.objects.first()
        cache.set("admin-data", admin_data, timeout=60 * 1440 * 30)

    _project = cache.get(f"project-{project_id}")
    if not _project:
        _project = Project.objects.filter(id=project_id).first()
        cache.set(f"project-{project_id}", _project, timeout=60 * 1440 * 30)

    _next_project = cache.get(f"project-{int(project_id) + 1}")
    if not _next_project:
        _next_project = str(Project.objects.filter(id=_project.next_id))
        cache.set(f"project-{project_id}", _next_project,
                  timeout=60 * 1440 * 30)

    return render(request, 'portfolio/project.html', {
        'id': project_id,
        'admin_data': admin_data,
        'project': _project,
        'next_project': _next_project,
    })
