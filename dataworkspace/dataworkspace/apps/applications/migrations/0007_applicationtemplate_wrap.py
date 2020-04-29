# Generated by Django 3.0.5 on 2020-04-30 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('applications', '0006_auto_20200430_1503')]

    operations = [
        migrations.AddField(
            model_name='applicationtemplate',
            name='wrap',
            field=models.CharField(
                choices=[
                    ('NONE', 'No wrapping'),
                    ('FULL_HEIGHT_IFRAME', 'Wrapped in full height iframe'),
                ],
                default='NONE',
                max_length=128,
            ),
        )
    ]
