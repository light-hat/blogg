# Generated by Django 4.0.1 on 2022-01-23 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_background_image_article_poster_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='poster_image',
        ),
        migrations.RemoveField(
            model_name='article',
            name='poster_image_check',
        ),
    ]
