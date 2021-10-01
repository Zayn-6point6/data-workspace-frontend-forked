# Generated by Django 3.2.4 on 2021-08-09 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0085_remove_datasetvisualisation_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='licence_url',
            field=models.CharField(
                blank=True,
                help_text='Link to license (optional)',
                max_length=1024,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='licence',
            field=models.CharField(
                blank=True, help_text='Licence description', max_length=256, null=True
            ),
        ),
    ]