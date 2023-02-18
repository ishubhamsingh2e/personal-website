from django.db import models
from django.urls import reverse


class Blog(models.Model):
    STATUS_CHOICE = {
        ('draft', 'draft'),
        ('published', 'published'),
    }

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=50)
    author_link = models.URLField()
    tags = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=(
        ("ui/ux", "UI"),
        ("machine learning", "ML"),
        ("development", "DEV"),
        ("research", "RE")
    ))
    sub_category = models.CharField(max_length=50, choices=(
        ("sorting-ui-ux", "UI"),
        ("sorting-ml", "ML"),
        ("sorting-development", "DEV"),
        ("sorting-research", "RE")
    ))
    hero_image = models.URLField()
    hero_image_alt = models.CharField(max_length=300, blank=True)
    meta_description = models.TextField()
    quote = models.TextField()
    body = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICE,
                              default='draft')

    def get_absolute_url(self):
        return reverse('article', args=[
            self.date.year,
            self.date.month,
            self.date.day,
            self.slug
        ])

    class Meta:
        ordering = ("-date",)

    def __str__(self):
        return f"{self.id}. {self.title}"

# Create your models here.
