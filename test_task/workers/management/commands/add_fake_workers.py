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

    def create_object(self, parent):
        obj = Employee.objects.create(name=seeder.faker.name(),
                                      job_title=seeder.faker.job(),
                                      salary=seeder.faker.pyfloat(left_digits=2, right_digits=2, positive=True),
                                      parent=parent)
        return obj

    def handle(self, *args, **options):
        workers_count = options['count']
        workers_count = 500
        second_level_count = workers_count // 100  # 500
        third_level_count = second_level_count * 5  # 2500 workers from second level
        fourth_level_count = third_level_count * 5  # 12500 workers from third level
        fifth_level_count = workers_count - (second_level_count + third_level_count + fourth_level_count)  # 34500
        parent = Employee.objects.first()
        for second_level_worker in range(second_level_count):
            # creating second level workers
            parent = self.create_object(parent)
            for third_level_worker in range(third_level_count):
                # creating third level workers
                parent = self.create_object(parent)
                for fourth_level_worker in range(fourth_level_count):
                    # creating fourth level workers
                    parent = self.create_object(parent)
                    for fifth_level_worker in range(fifth_level_count):
                        # creating fifth level workers
                        self.create_object(parent)
        # Employee.objects.rebuild()
        self.stdout.write(self.style.SUCCESS(f'{workers_count} workers created'))
