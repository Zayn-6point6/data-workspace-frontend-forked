# Generated by Django 3.2.15 on 2022-10-26 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data_collections", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="collection",
            name="published",
            field=models.BooleanField(default=False),
        ),
    ]