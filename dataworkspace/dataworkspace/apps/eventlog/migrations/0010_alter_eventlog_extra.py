# Generated by Django 3.2.4 on 2021-06-11 09:32

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventlog', '0009_auto_20210511_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventlog',
            name='extra',
            field=models.JSONField(
                encoder=django.core.serializers.json.DjangoJSONEncoder, null=True
            ),
        ),
    ]
