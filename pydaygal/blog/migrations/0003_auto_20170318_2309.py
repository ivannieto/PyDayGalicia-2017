# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 23:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170208_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='_content_ca_rendered',
        ),
        migrations.RemoveField(
            model_name='post',
            name='_content_en_rendered',
        ),
        migrations.RemoveField(
            model_name='post',
            name='_content_eu_rendered',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content_ca',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content_ca_markup_type',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content_en_markup_type',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content_eu',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content_eu_markup_type',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug_ca',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug_eu',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_ca',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title_eu',
        ),
    ]
