# Generated by Django 2.2.17 on 2021-02-23 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ropecon2021", "0001_initial"),
        ("programme", "0102_auto_20210222_2104"),
    ]

    operations = [
        migrations.AddField(
            model_name="programme",
            name="ropecon2021_blocked_time_slots",
            field=models.ManyToManyField(
                blank=True,
                help_text="Select the times when you are <b>NOT able</b> to run your larp. In other words, leave the times that you would be able to run your larp unselected!<br/>If you have a more specific request in mind regarding your schedule (for example, you would like to run your larp late at night), please let us know in the Comments section below.<br/>In this section, we would like to know more about how work or volunteer shifts, public transport schedules and other factors might be impacting your schedule. For example, if you need to leave the venue by 11pm to be able to catch the last bus to your accommodation.",
                related_name="_programme_ropecon2021_blocked_time_slots_+",
                to="ropecon2021.TimeSlot",
                verbose_name="When are you NOT able to run your game?",
            ),
        ),
    ]
