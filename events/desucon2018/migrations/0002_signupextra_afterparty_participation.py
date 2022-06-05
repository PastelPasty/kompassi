# Generated by Django 1.10.8 on 2018-06-02 18:30
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("desucon2018", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="signupextra",
            name="afterparty_participation",
            field=models.BooleanField(
                default=False,
                help_text="Ruksaa tämä ruutu, mikäli haluat osallistua kaatajaisiin. Mikäli mielesi muuttuu tai sinulle tulee este, peru ilmoittautumisesi poistamalla rasti tästä ruudusta.",
                verbose_name="Osallistun kaatajaisiin",
            ),
        ),
    ]
