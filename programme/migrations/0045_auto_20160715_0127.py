# Generated by Django 1.9.5 on 2016-07-14 22:27


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("programme", "0044_auto_20160712_1406"),
    ]

    operations = [
        migrations.AlterField(
            model_name="programme",
            name="category",
            field=models.ForeignKey(
                help_text="Choose the category that fits your programme the best. We reserve the right to change this.",
                on_delete=django.db.models.deletion.CASCADE,
                to="programme.Category",
                verbose_name="category",
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="number_of_microphones",
            field=models.IntegerField(
                choices=[
                    (0, "0"),
                    (1, "1"),
                    (2, "2"),
                    (3, "3"),
                    (4, "4"),
                    (5, "5"),
                    (
                        99,
                        'More than five \u2013 Please elaborate on your needs in the "Other tech requirements" field.',
                    ),
                ],
                default=1,
                help_text="How many microphones do you require?",
                verbose_name="Microphones",
            ),
        ),
    ]
