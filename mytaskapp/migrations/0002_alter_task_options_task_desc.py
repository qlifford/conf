# Generated by Django 4.2.7 on 2023-12-01 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytaskapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('updated',)},
        ),
        migrations.AddField(
            model_name='task',
            name='desc',
            field=models.CharField(default=0, max_length=1000),
        ),
    ]