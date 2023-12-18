# Generated by Django 4.1.7 on 2023-08-22 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('pos', models.CharField(max_length=50)),
                ('pronunciation', models.CharField(max_length=100)),
                ('meaning', models.TextField()),
            ],
        ),
    ]
