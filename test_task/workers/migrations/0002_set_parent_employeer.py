from django.db import migrations


# from test_task.workers.models import Employee

def _create_employee(site_model, name, job_title):
    """Update or create the site with default ID and keep the DB sequence in sync."""
    employee, created = site_model.objects.update_or_create(
        id=1,
        defaults={
            "job_title": job_title,
            "name": name,
        },
        salary=2000,
        parent=None,
        lft=1,
        rght=2,
        tree_id=1,
        level=0
    )
    if created:
        print("Successfully created")


def create_director_forward(apps, schema_editor):
    Employee = apps.get_model("workers", "Employee")
    _create_employee(
        Employee,
        "Каират Султан Марат улы",
        "Директор",
    )


def create_director_backward(apps, schema_editor):
    Employee = apps.get_model("workers", "Employee")
    _create_employee(
        Employee,
        "Family Name Surname",
        "Director",
    )


class Migration(migrations.Migration):
    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_director_forward, create_director_backward),
    ]
