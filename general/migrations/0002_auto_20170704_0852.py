# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-04 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='slide_num',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]