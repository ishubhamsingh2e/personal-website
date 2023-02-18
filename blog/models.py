from django.db import models
from django.urls import reverse


class Blog(models.Model):
    STATUS_CHOICE = {
        ('draft', 'draft'),
        ('published', 'published'),
    }

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    date = models.DateField()
    author = models.CharField(max_length=50)
    author_link = models.URLField()
    tags = models.CharField(max_length=100)
    cat = models.CharField(max_length=50, choices=(
        ("ui/ux", "UI"),
        ("machine learning", "ML"),
        ("development", "DEV"),
        ("research", "RE")
    ))
    cat_1 = models.CharField(max_length=50, choices=(
        ("sorting-ui-ux", "UI"),
        ("sorting-ml", "ML"),
        ("sorting-development", "DEV"),
        ("sorting-research", "RE")
    ))
    cat_2 = models.CharField(max_length=50, choices=(
        ("sorting-ui-ux", "UI"),
        ("sorting-ml", "ML"),
        ("sorting-development", "DEV"),
        ("sorting-research", "RE")
    ))
    hero_image = models.CharField(max_length=300)
    abstract = models.TextField()
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
