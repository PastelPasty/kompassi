# Generated by Django 2.2.27 on 2022-02-21 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("programme", "0106_auto_20210914_1548"),
    ]

    operations = [
        migrations.AddField(
            model_name="programme",
            name="ropecon2022_accessibility_remaining_one_place",
            field=models.BooleanField(
                default=False,
                verbose_name="Participation involves a lot of remaining in one place without a chance to take breaks and move around",
            ),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2022_aimed_at_adult_participants",
            field=models.BooleanField(
                default=False,
                help_text="Tick this box if your program is designed for adult participants.",
                verbose_name="Aimed at adult participants",
            ),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2022_aimed_at_children_under_10",
            field=models.BooleanField(
                default=False,
                help_text="Tick this box if your program is designed for children under the age of 10.",
                verbose_name="Aimed at children under 10 years old",
            ),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2022_aimed_at_underage_participants",
            field=models.BooleanField(
                default=False,
                help_text="Tick this box if your program is designed for underage participants.",
                verbose_name="Aimed at underage participants",
            ),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2022_content_warnings",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Examples: spiders, violence, phobias or other possibly triggering themes",
                max_length=1023,
                verbose_name="Tell us here if your game contains heavy subjects that may cause discomfort or distress in participants",
            ),
        ),
    ]
