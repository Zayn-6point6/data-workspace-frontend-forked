# Generated by Django 3.2.15 on 2022-11-01 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("data_collections", "0008_auto_20221031_1614"),
    ]

    operations = [
        migrations.RenameField(
            model_name="collection",
            old_name="catalogues",
            new_name="visualisation_catalogue_items",
        ),
    ]
