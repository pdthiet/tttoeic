# Generated by Django 4.1.7 on 2023-09-23 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VipPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField()),
                ('price', models.IntegerField()),
                ('sale_price', models.IntegerField()),
            ],
        ),
    ]
