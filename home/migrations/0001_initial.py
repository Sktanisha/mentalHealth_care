# Generated by Django 3.2.9 on 2022-02-26 19:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField(max_length=3)),
                ('address', models.CharField(max_length=100)),
                ('mobile', models.IntegerField(max_length=11)),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('confirm_password', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='msgs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=20)),
                ('person_email', models.CharField(max_length=20)),
                ('person_contact', models.IntegerField(max_length=11)),
                ('msg', models.CharField(max_length=1000)),
            ],
        ),
    ]