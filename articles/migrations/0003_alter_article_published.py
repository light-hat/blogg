# Generated by Django 4.0.1 on 2022-01-22 08:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_artpage_disclaimer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.DateField(default=datetime.date(2022, 1, 22), verbose_name='Дата публикации'),
        ),
    ]
