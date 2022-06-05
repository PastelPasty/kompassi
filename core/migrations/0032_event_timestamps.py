# Generated by Django 2.1.12 on 2019-09-06 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0031_person_badge_name_display_style"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
