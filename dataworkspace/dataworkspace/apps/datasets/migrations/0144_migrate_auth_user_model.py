# Generated by Django 3.2.19 on 2023-05-12 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0014_migrate_auth_user_model"),
        ("datasets", "0143_auto_20230511_1615"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datagrouping",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created+",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="datagrouping",
            name="information_asset_manager",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="asset_manager",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="datagrouping",
            name="information_asset_owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="asset_owner",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="datagrouping",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="updated+",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="dataset",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created+",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="dataset",
            name="enquiries_contact",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="dataset",
            name="information_asset_manager",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="info_asset_managed_datasets",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="dataset",
            name="information_asset_owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="info_asset_owned_datasets",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="dataset",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="updated+",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="datasetchartbuilderchart",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created+",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="datasetchartbuilderchart",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="updated+",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="datasetsubscription",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created+",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="datasetsubscription",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="updated+",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="datasetsubscription",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.dataworkspaceuser"
            ),
        ),
        migrations.AlterField(
            model_name="datasetvisualisation",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created+",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="datasetvisualisation",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="updated+",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="pipeline",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created+",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="pipeline",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="updated+",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="referencedataset",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created+",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="referencedataset",
            name="enquiries_contact",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="referencedataset",
            name="information_asset_manager",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="info_asset_managed_reference_datasets",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="referencedataset",
            name="information_asset_owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="info_asset_owned_reference_datasets",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="referencedataset",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="updated+",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="referencedatasetfield",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created+",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="referencedatasetfield",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="updated+",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="referencedatasetuploadlog",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created+",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="referencedatasetuploadlog",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="updated+",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="visualisationcatalogueitem",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="created+",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="visualisationcatalogueitem",
            name="enquiries_contact",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="visualisationcatalogueitem",
            name="information_asset_manager",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="info_asset_managed_visualisations",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="visualisationcatalogueitem",
            name="information_asset_owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="info_asset_owned_visualisations",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="visualisationcatalogueitem",
            name="secondary_enquiries_contact",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="core.dataworkspaceuser",
            ),
        ),
        migrations.AlterField(
            model_name="visualisationcatalogueitem",
            name="updated_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="updated+",
                to="core.dataworkspaceuser",
            ),
        ),
    ]