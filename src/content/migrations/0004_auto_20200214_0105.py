# Generated by Django 3.0.2 on 2020-02-13 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_drawing_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drawing',
            name='attributes',
        ),
        migrations.RemoveField(
            model_name='drawing',
            name='materials',
        ),
        migrations.RemoveField(
            model_name='drawing',
            name='size',
        ),
        migrations.RemoveField(
            model_name='drawing',
            name='tags',
        ),
    ]