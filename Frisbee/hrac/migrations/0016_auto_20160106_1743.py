# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrac', '0015_auto_20160106_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrac',
            name='pohlavie',
            field=models.CharField(default=b'Male', max_length=5, choices=[('Mu\u017e', 'Mu\u017e'), ('\u017dena', '\u017dena')]),
        ),
    ]