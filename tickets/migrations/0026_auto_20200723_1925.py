# Generated by Django 2.2.10 on 2020-07-23 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tickets", "0025_auto_20181130_0739"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="reference_number",
            field=models.CharField(blank=True, db_index=True, max_length=31, verbose_name="Viitenumero"),
        ),
    ]
