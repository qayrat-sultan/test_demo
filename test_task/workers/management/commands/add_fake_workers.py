from django_seed import Seed
from test_task.workers.models import Employee
from django.core.management.base import BaseCommand, CommandError

seeder = Seed.seeder()


class Command(BaseCommand):
    help = 'Add fake workers'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            nargs='?',
            default=30
        )

    def handle(self, *args, **options):
        workers_count = options['count']
        parent = Employee.objects.first()
        print(parent, parent.id)
        seeder.add_entity(Employee, workers_count), {
            'name': seeder.faker.name(),
            'job_title': seeder.faker.job(),
            'employment_date': seeder.faker.date_time_between(start_date='-30d', end_date='-1d'),
            'salary': seeder.faker.pyfloat(left_digits=2, right_digits=2, positive=True),
            'parent': parent,
        }
        seeder.execute()
        Employee.objects.rebuild()
