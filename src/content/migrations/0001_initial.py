# Generated by Django 3.0.2 on 2020-01-13 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drawing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('date', models.TextField()),
                ('size', models.TextField()),
                ('aditional', models.TextField()),
                ('sold', models.BooleanField(null=True)),
                ('tags', models.TextField()),
                ('materials', models.TextField()),
                ('attributes', models.TextField()),
                ('price', models.TextField()),
                ('shops', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='')),
            ],
        ),
    ]