# Generated by Django 4.1.7 on 2023-02-18 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_meta_description_blog_abstract_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='abstract',
            new_name='meta_description',
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('draft', 'draft'), ('published', 'published')], default='draft', max_length=10),
        ),
    ]
