# Generated by Django 4.1.4 on 2022-12-17 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0037_alter_organization_panel_css_class"),
        ("labour", "0034_archivedsignup"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="personnelclass",
            name="perks",
        ),
        migrations.AddField(
            model_name="personnelclass",
            name="perks_markdown",
            field=models.TextField(
                blank=True,
                default="",
                help_text="Focus on things that are given to the person at check-in. Markdown formatting available.",
                verbose_name="perks",
            ),
        ),
        migrations.AlterField(
            model_name="emptysignupextra",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="%(app_label)s_signup_extras", to="core.event"
            ),
        ),
        migrations.AlterField(
            model_name="emptysignupextra",
            name="person",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, related_name="%(app_label)s_signup_extra", to="core.person"
            ),
        ),
        migrations.AlterField(
            model_name="laboureventmeta",
            name="event",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                related_name="%(class)s",
                serialize=False,
                to="core.event",
            ),
        ),
        migrations.AlterField(
            model_name="obsoleteemptysignupextrav1",
            name="signup",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                related_name="%(app_label)s_signup_extra",
                serialize=False,
                to="labour.signup",
            ),
        ),
        migrations.AlterField(
            model_name="signup",
            name="job_categories_rejected",
            field=models.ManyToManyField(
                blank=True,
                help_text="The workforce manager may use this field to inform other workforce managers that this applicant will not be accepted to a certain job category. This field is not visible to the applicant, but should they request a record of their own information, this field will be included.",
                related_name="+",
                to="labour.jobcategory",
                verbose_name="Rejected job categories",
            ),
        ),
        migrations.DeleteModel(
            name="Perk",
        ),
    ]
