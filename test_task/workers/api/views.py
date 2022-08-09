from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from test_task.workers.api.serializers import EmployeeSerializer
from test_task.workers.models import Employee


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.viewable()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
