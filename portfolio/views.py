from django.shortcuts import render
from .models import *
from blog.models import Blog

from django.views.decorators.cache import cache_page
from django.core.cache import cache


# Create your views here.

def index(request):
    services = Service.objects.all()
    skills = Skill.objects.all()
    admin_data = AdminData.objects.first()
    education = StoryEducation.objects.all().order_by("id").reverse()
    experience = StoryExperience.objects.all().order_by("id").reverse()
    _project = Project.objects.all()
    education_last = len(education)
    experience_last = len(experience)
    _blog = Blog.objects.all()[:3]
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


def project(request, project_id):
    admin_data = AdminData.objects.first()
    _project = Project.objects.filter(id=project_id).first()
    _next_project = str(Project.objects.filter(id=_project.next_id))
    return render(request, 'portfolio/project.html', {
        'id': project_id,
        'admin_data': admin_data,
        'project': _project,
        'next_project': _next_project,
    })
