# Generated by Django 2.2.4 on 2019-12-02 15:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [('datasets', '0024_auto_20191118_1349')]

    operations = [
        migrations.AlterField(
            model_name='referencedataset',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        )
    ]
