# Generated by Django 4.2.7 on 2024-01-11 14:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0009_alter_blog_author_alter_blog_created_delete_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 11, 17, 6, 22, 882344)),
        ),
    ]
