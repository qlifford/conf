# Generated by Django 4.2.7 on 2024-01-09 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_blog_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='user',
        ),
    ]
