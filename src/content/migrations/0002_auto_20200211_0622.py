# Generated by Django 3.0.2 on 2020-02-11 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drawing',
            name='aditional',
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainimage', models.ImageField(null=True, upload_to='img')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Drawing')),
            ],
        ),
    ]