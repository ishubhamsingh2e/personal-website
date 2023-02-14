from django.db import models
from taggit.managers import TaggableManager


# Create your models here.

class AdminData(models.Model):
    bio = models.TextField()
    cvLink = models.TextField()
    userName = models.TextField(max_length=50)
    email = models.CharField(max_length=50)
    github = models.CharField(max_length=100)
    dev = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    blog_category = TaggableManager()


class Service(models.Model):
    field = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()


class Skill(models.Model):
    skill = models.CharField(max_length=50)
    level = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.id}: {self.skill}"


class StoryEducation(models.Model):
    place = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    description = models.TextField()
    syear = models.IntegerField()
    eyear = models.IntegerField()


class StoryExperience(models.Model):
    place = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    description = models.TextField()
    syear = models.DateField()
    eyear = models.DateField()


# project models

class Project(models.Model):
    title = models.CharField(max_length=150)
    time = models.DateField()
    technology = models.CharField(max_length=300)
    categories = models.CharField(max_length=300)
    description_small = models.TextField(max_length=150)
    project_url = models.URLField()
    hero_image = models.URLField()
    description_left = models.TextField()
    description_right = models.TextField()
    portrait = models.URLField()
    landscape_top = models.URLField()
    landscape_bottom = models.URLField()
    conclusion_left = models.TextField()
    conclusion_right = models.TextField()
    video = models.URLField()
    next_id = models.IntegerField(null=True)
    next_name = models.CharField(max_length=150, null=True)
    sort_1 = models.CharField(max_length=50, choices=(
        ("sorting-ui-ux", "UI"),
        ("sorting-ml", "ML"),
        ("sorting-development", "DEV"),
        ("sorting-research", "RE")
    ))
    sort_2 = models.CharField(max_length=50, choices=(
        ("sorting-ui-ux", "UI"),
        ("sorting-ml", "ML"),
        ("sorting-development", "DEV"),
        ("sorting-research", "RE")
    ))
