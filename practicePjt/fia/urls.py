from django.urls import path
from . import views

urlpatterns = [
    path("", views.fia, name="fia"),
    path("<int:fiadetail_id>", views.fiadetail, name="fiadetail"),
    path("<int:fiadetail_id>/evaluate", views.fiaeval, name="fiaeval"),
    path("<int:fiadetail_id>/save", views.save, name="save"),
    path(
        "delete_request/<int:fiadetail_id>/<int:fiaeval_id>",
        views.delete_request,
        name="delete_request",
    ),
    path("delete/<int:fiadetail_id>/<int:fiaeval_id>", views.delete, name="delete"),
    path(
        "update_request/<int:fiadetail_id>/<int:fiaeval_id>",
        views.update_request,
        name="update_request",
    ),
    path("update/<int:fiadetail_id>/<int:fiaeval_id>", views.update, name="update"),
    path(
        "updateFinal/<int:fiadetail_id>/<int:fiaeval_id>",
        views.updateFinal,
        name="updateFinal",
    ),
]
