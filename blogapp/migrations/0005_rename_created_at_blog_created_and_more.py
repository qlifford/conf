# Generated by Django 4.2.7 on 2023-12-04 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_blog_created_at_blog_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='updated_at',
            new_name='updated',
        ),
    ]