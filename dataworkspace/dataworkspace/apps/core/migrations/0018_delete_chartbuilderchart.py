# Generated by Django 3.2.23 on 2023-12-21 11:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("datasets", "0161_delete_datasetchartbuilderchart"),
        ("core", "0017_team_notes"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ChartBuilderChart",
        ),
    ]
