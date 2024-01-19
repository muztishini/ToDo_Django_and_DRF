from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'api/task', TaskViewSet)

urlpatterns = [
  path("", index),
  path("add_task", add_task, name="add_task"),
  path("edit_task/<int:id>/", edit_task, name="edit_task"),
  path("delete_task/<int:id>/", delete_task, name="delete_task"),
  path('', include(router.urls)),
]
