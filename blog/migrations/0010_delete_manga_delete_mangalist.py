# Generated by Django 4.2.4 on 2023-08-31 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_mangalist_manga_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Manga',
        ),
        migrations.DeleteModel(
            name='MangaList',
        ),
    ]
