from django.urls import path
from . import views

urlpatterns = [
    path("test", views.tset),
    path(
        "create-course-evaluation/<int:course_id>",
        views.create_course_evaluation,
        name="create-course-evaluation",
    ),
]
