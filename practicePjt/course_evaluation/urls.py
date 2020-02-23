from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("search-course", views.search_course, name="search-course"),
    path(
        "create-course-evaluation/<int:course_id>",
        views.create_course_evaluation,
        name="create-course-evaluation",
    ),
]
