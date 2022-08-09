from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.managers import TreeManager
from mptt.models import MPTTModel, TreeForeignKey


class EmployeeManager(TreeManager):
    def viewable(self):
        queryset = self.get_queryset().filter(level=0)
        return queryset


class Employee(MPTTModel):
    name = models.CharField(_("ФИО работника"), max_length=100)
    job_title = models.CharField(_("Должность"), max_length=100)
    employment_date = models.DateField(_("Дата приема на работу"), default=timezone.now)
    salary = models.FloatField(_("Размер зарплаты"))
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    objects = EmployeeManager()

    def __str__(self):
        return self.name

    class MPTTMeta:
        db_table = 'employee'
        order_insertion_by = ['name']
