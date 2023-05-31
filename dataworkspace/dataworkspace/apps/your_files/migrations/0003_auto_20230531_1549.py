# Generated by Django 3.2.19 on 2023-05-31 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("your_files", "0002_migrate_auth_user_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="uploadedtable",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="uploadedtable",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="updated+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
