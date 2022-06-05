# Generated by Django 2.1.12 on 2019-09-09 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("surveys", "0003_auto_20180330_1812"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventsurveyresult",
            name="survey",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="results", to="surveys.EventSurvey"
            ),
        ),
        migrations.AlterField(
            model_name="globalsurveyresult",
            name="survey",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="results", to="surveys.GlobalSurvey"
            ),
        ),
    ]
