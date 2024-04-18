# Generated by Django 5.0.4 on 2024-04-08 12:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0040_rename_emailverificationtoken_person_state_core_emailv_person__722147_idx_and_more"),
        ("hitpoint2017", "0005_delete_signupextra"),
        ("hitpoint2020", "0004_alter_signupextra_signup"),
        ("paikkala", "0016_zone_ordering"),
        ("programme", "0126_programmeeventmeta_override_schedule_link_and_more"),
        ("ropecon2018", "0003_alter_signupextra_signup"),
        ("ropecon2019", "0005_alter_signupextra_event_alter_signupextra_person"),
        ("ropecon2021", "0002_alter_signupextra_event_alter_signupextra_person"),
        ("ropecon2023", "0002_language_remove_signupextra_can_english_and_more"),
        ("ropecon2024", "0001_initial"),
        ("solmukohta2024", "0002_technology"),
        ("tracon2023", "0003_signupextraafterpartyproxy_and_more"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="programme",
            index=models.Index(fields=["category", "slug"], name="programme_p_categor_5b8eeb_idx"),
        ),
    ]