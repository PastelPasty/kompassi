# Generated by Django 1.9.4 on 2016-04-06 15:28


from django.db import migrations, models


def fix_signup_extra_form_class_paths(apps, schema_editor):
    AlternativeSignupForm = apps.get_model("labour", "alternativesignupform")
    AlternativeSignupForm.objects.filter(signup_extra_form_class_path="labour.forms:EmptySignupExtraForm").update(
        signup_extra_form_class_path="labour.forms:ObsoleteEmptySignupExtraV1Form"
    )


class Migration(migrations.Migration):

    dependencies = [
        ("labour", "0022_rename_empty_signup_extra"),
    ]

    operations = [
        migrations.AlterField(
            model_name="alternativesignupform",
            name="signup_extra_form_class_path",
            field=models.CharField(
                default="labour.forms:ObsoleteEmptySignupExtraV1Form",
                help_text="Viittaus lis\xe4tietolomakkeen toteuttavaan luokkaan. Esimerkki: tracon9.forms:ConcomSignupExtraForm",
                max_length=63,
            ),
        ),
        migrations.RunPython(fix_signup_extra_form_class_paths, elidable=True),
    ]
