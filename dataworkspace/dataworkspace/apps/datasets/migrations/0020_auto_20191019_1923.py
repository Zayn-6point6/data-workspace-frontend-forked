# Generated by Django 2.2.4 on 2019-10-19 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('datasets', '0019_merge_20191019_1154')]

    operations = [
        migrations.AlterField(
            model_name='referencedataset',
            name='is_joint_dataset',
            field=models.BooleanField(default=False),
        )
    ]
