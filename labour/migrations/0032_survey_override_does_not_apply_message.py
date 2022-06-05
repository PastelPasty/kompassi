# Generated by Django 1.9.9 on 2016-09-07 19:11


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("labour", "0031_surveyrecord"),
    ]

    operations = [
        migrations.AddField(
            model_name="survey",
            name="override_does_not_apply_message",
            field=models.TextField(
                default="",
                help_text="This message will be shown to the user when they attempt to access a query they don'thave access to.",
                verbose_name="Message when denied access",
            ),
        ),
    ]
