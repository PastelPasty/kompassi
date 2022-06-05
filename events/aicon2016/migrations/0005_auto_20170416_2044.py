# Generated by Django 1.10.6 on 2017-04-16 17:44
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aicon2016", "0004_signupextra_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="signupextra",
            name="shift_type",
            field=models.CharField(
                choices=[
                    ("yksipitka", "Yksi pitkä vuoro"),
                    ("montalyhytta", "Monta lyhyempää vuoroa"),
                    ("kaikkikay", "Kumpi tahansa käy"),
                ],
                help_text="Haluatko tehdä yhden pitkän työvuoron vaiko monta lyhyempää vuoroa?",
                max_length=15,
                verbose_name="Toivottu työvuoron pituus",
            ),
        ),
        migrations.AlterField(
            model_name="signupextra",
            name="total_work",
            field=models.CharField(
                choices=[
                    ("8h", "Minimi - 8 tuntia"),
                    ("12h", "10–12 tuntia"),
                    ("yli12h", "Työn Sankari! Yli 12 tuntia!"),
                ],
                help_text="Kuinka paljon haluat tehdä töitä yhteensä tapahtuman aikana? Useimmissa tehtävistä minimi on kahdeksan tuntia, mutta joissain tehtävissä se voi olla myös vähemmän (esim. majoitusvalvonta 6 h).",
                max_length=15,
                verbose_name="Toivottu kokonaistyömäärä",
            ),
        ),
    ]
