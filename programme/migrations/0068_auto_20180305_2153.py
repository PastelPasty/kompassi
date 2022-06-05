# Generated by Django 1.10.8 on 2018-03-05 19:53
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("programme", "0067_auto_20180219_2222"),
    ]

    operations = [
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_audience_size",
            field=models.CharField(
                choices=[
                    ("unknown", "No estimate"),
                    ("lt50", "Less than 50"),
                    ("50-100", "50 - 100"),
                    ("100-150", "100 - 150"),
                    ("150-200", "150 - 200"),
                    ("200-250", "200 - 250"),
                    ("gt250", "Over 250"),
                ],
                default="unknown",
                help_text="Estimate of audience size for talk/presentation, if you have previous experience.",
                max_length=7,
                null=True,
                verbose_name="Audience estimate",
            ),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_characters",
            field=models.PositiveIntegerField(
                default=10,
                help_text="If the game design requires characters with a specific gender let us know in the notes.",
                null=True,
                validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999)],
                verbose_name="number of characters",
            ),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_genre_drama",
            field=models.BooleanField(default=False, verbose_name="Drama"),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_genre_exploration",
            field=models.BooleanField(default=False, verbose_name="Exploration"),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_genre_fantasy",
            field=models.BooleanField(default=False, verbose_name="Fantasy"),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_genre_historical",
            field=models.BooleanField(default=False, verbose_name="Historical"),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_genre_horror",
            field=models.BooleanField(default=False, verbose_name="Horror"),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_genre_humor",
            field=models.BooleanField(default=False, verbose_name="Humor"),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_genre_modern",
            field=models.BooleanField(default=False, verbose_name="Modern"),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_genre_mystery",
            field=models.BooleanField(default=False, verbose_name="Mystery"),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_genre_scifi",
            field=models.BooleanField(default=False, verbose_name="Sci-fi"),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_genre_war",
            field=models.BooleanField(default=False, verbose_name="War"),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_is_no_language",
            field=models.BooleanField(
                default=False, help_text="No Finnish language needed to participate.", verbose_name="No language"
            ),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_is_panel_attendance_ok",
            field=models.BooleanField(
                default=False,
                help_text="I can participate in a panel discussion related to my field of expertise.",
                verbose_name="Panel talk",
            ),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_prop_requirements",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Let us know what props and other equipment you need. Not all requests can be accommodated. Water and glasses are always provided.",
                max_length=200,
                null=True,
                verbose_name="Prop requirements",
            ),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_sessions",
            field=models.PositiveIntegerField(
                default=2,
                help_text="This is your preference only. Due to the limited space we are not able to accommodate all requests. One four hour session gives you one weekend ticket. A second session gives you an additional day ticket.",
                null=True,
                validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999)],
                verbose_name="number of sessions",
            ),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_signuplist",
            field=models.CharField(
                choices=[("itse", "I will make my own signup sheet"), ("tiski", "Desk will make the signup sheet")],
                default="itse",
                help_text="A self-made signup sheet allows you to ask more detailed player preferences. Larp-desk-made signup sheet is a list of participant names.",
                max_length=15,
                null=True,
                verbose_name="Do you make your own signup sheet",
            ),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_space_requirements",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Let us know of your requirements. Fully dark, separate rooms, water outlet, etc.",
                max_length=200,
                null=True,
                verbose_name="Space requirements",
            ),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_speciality",
            field=models.CharField(
                blank=True, default="", max_length=100, null=True, verbose_name="My field(s) of expertise"
            ),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_style_character_driven",
            field=models.BooleanField(default=False, verbose_name="Character driven"),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_style_combat_driven",
            field=models.BooleanField(default=False, verbose_name="Combat driven"),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_style_light",
            field=models.BooleanField(default=False, verbose_name="Light game style"),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_style_rules_heavy",
            field=models.BooleanField(default=False, verbose_name="Rules heavy"),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_style_rules_light",
            field=models.BooleanField(default=False, verbose_name="Rules light"),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_style_serious",
            field=models.BooleanField(default=False, verbose_name="Serious game style"),
        ),
        migrations.AddField(
            model_name="programme",
            name="ropecon2018_style_story_driven",
            field=models.BooleanField(default=False, verbose_name="Story driven"),
        ),
    ]
