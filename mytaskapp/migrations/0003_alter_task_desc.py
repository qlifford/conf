# Generated by Django 4.2.7 on 2023-12-01 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytaskapp', '0002_alter_task_options_task_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='desc',
            field=models.CharField(max_length=1000),
        ),
    ]
