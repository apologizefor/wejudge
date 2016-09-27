# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-16 07:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20160709_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.CharField(default=b'', max_length=10)),
                ('studentPwd', models.CharField(default=b'', max_length=200)),
                ('studentName', models.CharField(default=b'', max_length=20)),
                ('grade', models.SmallIntegerField(default=2014)),
                ('sex', models.CharField(default=b'\xe6\x9c\xaa\xe7\x9f\xa5', max_length=2)),
                ('className', models.CharField(default=b'', max_length=20)),
                ('department', models.CharField(default=b'', max_length=20)),
                ('major', models.CharField(default=b'', max_length=20)),
                ('rawData', models.TextField(default=b'')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.User')),
            ],
        ),
    ]