# Generated by Django 4.1.7 on 2023-09-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0002_examination'),
    ]

    operations = [
        migrations.AddField(
            model_name='examination',
            name='audio_url',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='examination',
            name='image_url',
            field=models.TextField(null=True),
        ),
    ]
