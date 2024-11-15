from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (
    HabitCreateAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
    HabitListAPIView,
    HabitRetrieveAPIView,
    PublicHabitListAPIView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path("habits/create/", HabitCreateAPIView.as_view(), name="habits-create"),
    path("habits/<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habits-update"),
    path(
        "habits/<int:pk>/destroy/", HabitDestroyAPIView.as_view(), name="habits-destroy"
    ),
    path("habits/", HabitListAPIView.as_view(), name="habits-list"),
    path("habits/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habits-retrieve"),
    path("public/", PublicHabitListAPIView.as_view(), name="public"),
]