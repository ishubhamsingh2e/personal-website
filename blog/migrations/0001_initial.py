# Generated by Django 4.1.7 on 2023-02-18 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.CharField(max_length=50)),
                ('author_link', models.URLField()),
                ('tags', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('ui/ux', 'UI'), ('machine learning', 'ML'), ('development', 'DEV'), ('research', 'RE')], max_length=50)),
                ('sub_category', models.CharField(choices=[('sorting-ui-ux', 'UI'), ('sorting-ml', 'ML'), ('sorting-development', 'DEV'), ('sorting-research', 'RE')], max_length=50)),
                ('hero_image', models.URLField()),
                ('hero_image_alt', models.CharField(blank=True, max_length=300)),
                ('meta_description', models.TextField()),
                ('body', models.TextField()),
                ('status', models.CharField(choices=[('published', 'published'), ('draft', 'draft')], default='draft', max_length=10)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
