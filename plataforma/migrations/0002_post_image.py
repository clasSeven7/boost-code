# Generated by Django 5.1.1 on 2024-09-11 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
