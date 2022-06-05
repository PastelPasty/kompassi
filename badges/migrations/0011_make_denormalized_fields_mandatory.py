# Generated by Django 1.9.1 on 2016-01-29 19:59


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("badges", "0010_populate_denormalized_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="badge",
            name="first_name",
            field=models.CharField(max_length=1023, verbose_name="First name"),
        ),
        migrations.AlterField(
            model_name="badge",
            name="nick",
            field=models.CharField(blank=True, help_text="Nick name", max_length=1023),
        ),
        migrations.AlterField(
            model_name="badge",
            name="surname",
            field=models.CharField(max_length=1023, verbose_name="Surname"),
        ),
    ]
