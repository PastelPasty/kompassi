# Generated by Django 1.10.7 on 2017-05-01 20:30
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("surveys", "0002_auto_20170321_2103"),
        ("event_log", "0002_auto_20170416_2048"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="event_survey_filter",
            field=models.ForeignKey(
                blank=True,
                help_text="When specified, only entries related to this EventSurvey will match the subscription.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="surveys.EventSurvey",
                verbose_name="Event survey filter",
            ),
        ),
    ]
