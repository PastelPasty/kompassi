# Generated by Django 1.9.9 on 2016-11-29 19:47


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hitpoint2017", "0002_signupextra_is_active"),
    ]

    operations = [
        migrations.CreateModel(
            name="TimeSlot",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=63)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
