# Generated by Django 3.2.10 on 2022-01-07 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0020_alter_chartbuilderchart_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chartbuilderchart',
            name='original_query_log',
        ),
    ]
