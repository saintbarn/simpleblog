# Generated by Django 4.1.4 on 2022-12-25 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Click link above to read blog post...', max_length=255),
        ),
    ]
