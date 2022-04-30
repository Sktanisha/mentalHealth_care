# Generated by Django 2.1.3 on 2022-04-02 18:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220324_0042'),
    ]

    operations = [
        migrations.CreateModel(
            name='psychiatrist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=30)),
                ('ps_email', models.EmailField(max_length=30)),
                ('ps_mobile', models.IntegerField(max_length=11)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='quizresult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('result', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='accounts',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='msgs',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]