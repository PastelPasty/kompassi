# Generated by Django 2.1.12 on 2019-09-29 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hitpoint2019", "0002_auto_20190909_2157"),
    ]

    operations = [
        migrations.AddField(
            model_name="signupextra",
            name="shirt_size",
            field=models.CharField(
                choices=[
                    ("NO_SHIRT", "Ei paitaa"),
                    ("BOTTLE", "Juomapullo"),
                    ("XS", "XS Unisex"),
                    ("S", "S Unisex"),
                    ("M", "M Unisex"),
                    ("L", "L Unisex"),
                    ("XL", "XL Unisex"),
                    ("XXL", "XXL Unisex"),
                    ("3XL", "3XL Unisex"),
                    ("4XL", "4XL Unisex"),
                    ("5XL", "5XL Unisex"),
                    ("LF_XS", "XS Ladyfit"),
                    ("LF_S", "S Ladyfit"),
                    ("LF_M", "M Ladyfit"),
                    ("LF_L", "L Ladyfit"),
                    ("LF_XL", "XL Ladyfit"),
                ],
                default="NO_SHIRT",
                help_text='Ajoissa ilmoittautuneet vänkärit saavat maksuttoman työvoimapaidan. Valitse tässä paidan koko. Kokotaulukot: <a href="http://www.bc-collection.eu/uploads/sizes/TU004.jpg" target="_blank">unisex-paita</a>, <a href="http://www.bc-collection.eu/uploads/sizes/TW040.jpg" target="_blank">ladyfit-paita</a>',
                max_length=8,
                verbose_name="Paidan koko",
            ),
        ),
    ]
