# Generated by Django 4.1.7 on 2023-09-15 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0003_conversionscore'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examresult',
            old_name='grade',
            new_name='listening_score',
        ),
        migrations.AddField(
            model_name='examresult',
            name='reading_score',
            field=models.IntegerField(null=True),
        ),
    ]
