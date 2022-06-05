# Generated by Django 1.10.7 on 2017-07-22 16:54
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0024_carouselslide"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="carouselslide",
            options={
                "ordering": ("order", "active_from"),
                "verbose_name": "carousel slide",
                "verbose_name_plural": "carousel slides",
            },
        ),
        migrations.AddField(
            model_name="carouselslide",
            name="order",
            field=models.IntegerField(default=0),
        ),
    ]
