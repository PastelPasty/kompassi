# Generated by Django 2.1.8 on 2019-06-14 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("programme", "0091_role_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="programmefeedback",
            name="author_external_username",
            field=models.CharField(blank=True, default="", max_length=150, verbose_name="External username"),
        ),
    ]
