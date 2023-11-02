import re
from django.db import migrations

skip_items = [
    "great.gov.uk value for money survey responses",
    "DDaT Recruitment Survey",
    "Regional inbound enquiries 2018-2020",
    "DDaT Return to the office survey",
    "DIT MS Teams feedback survey",
    "Civil Service Leadership Academy Training Records",
    "Jobs supported by UK exports",
    "DIT staff and contractors: leavers",
    "HR People Data merged 13 month rolling",
    "People Data: Cyber team report",
    "DIT staff and contractors: leavers",
    "DIT people data: joiners and leavers",
    "DIT Return to office: Personal Risk Assessment (PRA) data",
]
dit = "DIT"
dbt = "DBT"
dit_full = "Department for International Trade"
dbt_full = "Department for Business and Trade"
dit_full_low = "department for international trade"


def search_and_replace_eligibility_criteria(model):
    for dataset in model.objects.exclude(name__in=skip_items).all():
        if dataset.eligibility_criteria:
            eligibility_criteria = [
                criteria.replace(dit, dbt) for criteria in list(dataset.eligibility_criteria)
            ]
            dataset.eligibility_criteria = eligibility_criteria
            dataset.save()
            eligibility_criteria = [
                criteria.replace(dit_full, dbt_full)
                for criteria in list(dataset.eligibility_criteria)
            ]
            dataset.eligibility_criteria = eligibility_criteria
            dataset.save()
            eligibility_criteria = [
                criteria.replace(dit_full_low, dbt_full)
                for criteria in list(dataset.eligibility_criteria)
            ]
            dataset.eligibility_criteria = eligibility_criteria
            dataset.save()


def search_and_replace_eligibility_criteria_catalogue_items(apps, _):
    model = apps.get_model("datasets", "DataSet")
    search_and_replace_eligibility_criteria(model)

    model = apps.get_model("datasets", "VisualisationCatalogueItem")
    search_and_replace_eligibility_criteria(model)


class Migration(migrations.Migration):
    dependencies = [
        ("datasets", "0154_vis_dataset_m2m_seq"),
    ]

    operations = [
        migrations.RunPython(
            search_and_replace_eligibility_criteria_catalogue_items,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
