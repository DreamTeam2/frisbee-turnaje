# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turnaj',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nazov', models.CharField(max_length=50)),
                ('datum_od', models.DateField()),
                ('datum_do', models.DateField()),
                ('spirit', models.BooleanField()),
            ],
        ),
    ]