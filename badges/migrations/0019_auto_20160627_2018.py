# Generated by Django 1.9.5 on 2016-06-27 17:18


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("badges", "0018_badge_arrived_at"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="batch",
            options={"verbose_name": "Batch"},
        ),
        migrations.AlterField(
            model_name="badge",
            name="batch",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="badges.Batch",
                verbose_name="Printing batch",
            ),
        ),
    ]
