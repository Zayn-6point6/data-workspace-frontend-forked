# Generated by Django 3.2.15 on 2022-09-26 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("request_data", "0004_datarequest_data_licence"),
    ]

    operations = [
        migrations.RenameField(
            model_name="datarequest",
            old_name="zendesk_ticket_id",
            new_name="help_desk_ticket_id",
        ),
    ]
