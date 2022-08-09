from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from test_task.users.api.views import UserViewSet
from test_task.workers.api.views import EmployeeViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("employees", EmployeeViewSet)


app_name = "api"
urlpatterns = router.urls
