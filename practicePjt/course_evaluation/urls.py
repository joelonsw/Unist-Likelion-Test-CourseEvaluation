from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("search-course", views.search_course, name="search-course")
    
    path("<int:course_id>", views.detail, name="detail"),
    path("<int:course_id>/evaluate", views.evaluation, name="evaluation"),
    path("<int:course_id>/save", views.save, name="save"),
    path("<int:eval_id>/delete_request", views.delete_request, name="delete_request"),
    path("<int:eval_id>/delete", views.delete, name="delete"),
    path("<int:eval_id>/update_request", views.update_request, name="update_request"),
    path("<int:eval_id>/update",views.update, name="update"),
    path("<int:eval_id>/update_final", views.update_final, name="update_final"),

]