# Generated by Django 1.10.8 on 2018-04-29 17:11
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("programme", "0072_programme_language_skills"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="programme",
            name="language_skills",
        ),
    ]
