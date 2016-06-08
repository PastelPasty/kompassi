# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 20:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('programme', '0033_auto_20160608_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmeeventmeta',
            name='contact_email',
            field=models.CharField(blank=True, help_text='Kaikki ohjelmaj\xe4rjestelm\xe4n l\xe4hett\xe4m\xe4t s\xe4hk\xf6postiviestit l\xe4hetet\xe4\xe4n t\xe4st\xe4 osoitteesta, ja t\xe4m\xe4 osoite n\xe4ytet\xe4\xe4n ohjelmanj\xe4rjest\xe4j\xe4lle yhteysosoitteena. Muoto: Selite &lt;osoite@esimerkki.fi&gt;.', max_length=255, validators=[django.core.validators.RegexValidator(re.compile('(?P<name>.+) <(?P<email>.+@.+\\..+)>'))], verbose_name='yhteysosoite'),
        ),
    ]
