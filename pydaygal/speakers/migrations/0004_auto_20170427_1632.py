# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-27 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0003_auto_20170424_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='speakers', verbose_name='Fotografía'),
        ),
    ]