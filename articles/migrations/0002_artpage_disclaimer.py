# Generated by Django 4.0.1 on 2022-01-18 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artpage',
            name='disclaimer',
            field=models.TextField(default='', verbose_name='Дисклеймер'),
        ),
    ]