# Generated by Django 4.2.7 on 2024-04-26 10:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("applications", "0025_applicationtemplate_include_in_dw_stats"),
    ]

    operations = [
        migrations.CreateModel(
            name="ApplicationInstanceArangoUsers",
            fields=[
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("modified_date", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("db_username", models.CharField(max_length=256)),
                (
                    "application_instance",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="applications.applicationinstance",
                    ),
                ),
            ],
            options={
                "indexes": [
                    models.Index(fields=["db_username"], name="arangodb_ap_db_user_793637_idx")
                ],
            },
        ),
    ]
