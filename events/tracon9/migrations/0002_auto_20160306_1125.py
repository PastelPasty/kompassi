# Generated by Django 1.9.1 on 2016-03-06 09:25


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tracon9", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="signupextra",
            name="signup",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                related_name="tracon9_signup_extra",
                serialize=False,
                to="labour.Signup",
            ),
        ),
    ]
