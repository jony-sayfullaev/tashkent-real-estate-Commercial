# Generated by Django 4.1.5 on 2023-01-31 08:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listings', models.CharField(max_length=200)),
                ('listing_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 31, 8, 45, 48, 676400))),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
    ]