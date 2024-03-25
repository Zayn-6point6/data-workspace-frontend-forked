# Generated by Django 4.2.7 on 2024-03-25 13:15

from django.db import migrations


def unpublish_dit_source_tables(apps, _):
    source_table_model = apps.get_model("datasets", "SourceTable")
    for source_table in source_table_model.objects.filter(schema="dit").all():
        source_table.published = False
        source_table.save()


class Migration(migrations.Migration):
    dependencies = [
        ("datasets", "0166_sourcetable_published"),
    ]

    operations = [
        migrations.RunPython(unpublish_dit_source_tables, reverse_code=migrations.RunPython.noop),
    ]
