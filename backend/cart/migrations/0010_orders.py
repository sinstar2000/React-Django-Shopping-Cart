# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 12:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0009_auto_20171207_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('SN', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
