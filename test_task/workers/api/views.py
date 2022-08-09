from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from test_task.workers.api.serializers import EmployeeSerializer
from test_task.workers.models import Employee
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.viewable()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination
