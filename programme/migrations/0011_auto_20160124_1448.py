# Generated by Django 1.9.1 on 2016-01-24 12:48


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("programme", "0010_auto_20160123_1733"),
    ]

    operations = [
        migrations.AddField(
            model_name="invitation",
            name="code",
            field=models.CharField(default="", max_length=63, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="invitation",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="invitation",
            name="state",
            field=models.CharField(
                choices=[("valid", "Valid"), ("used", "Used"), ("revoked", "Revoked")], default="valid", max_length=8
            ),
        ),
        migrations.AddField(
            model_name="invitation",
            name="used_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="invitation",
            name="email",
            field=models.EmailField(blank=True, max_length=255, verbose_name="E-mail address"),
        ),
        migrations.AlterField(
            model_name="programmeedittoken",
            name="state",
            field=models.CharField(
                choices=[("valid", "Valid"), ("used", "Used"), ("revoked", "Revoked")], default="valid", max_length=8
            ),
        ),
    ]
