# Generated by Django 2.2.2 on 2019-07-05 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20190626_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourceschema',
            name='dataset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.DataSet'),
        ),
    ]
