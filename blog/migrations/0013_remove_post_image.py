# Generated by Django 4.2.4 on 2024-01-04 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]