# Generated by Django 4.1.4 on 2022-12-24 05:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('theblog', '0004_category_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
