# Generated by Django 4.2.7 on 2024-01-11 08:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_alter_blog_created_alter_blog_title_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
        migrations.AlterField(
            model_name='blog',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 11, 11, 26, 28, 545950)),
        ),
    ]
