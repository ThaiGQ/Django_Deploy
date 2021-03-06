# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 17:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel_Companions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('companion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_name', models.CharField(max_length=255)),
                ('trip_destination', models.CharField(max_length=100)),
                ('trip_description', models.TextField(max_length=1000)),
                ('trip_begin', models.DateTimeField()),
                ('trip_end', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.User')),
            ],
        ),
        migrations.AddField(
            model_name='travel_companions',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Trip'),
        ),
    ]
