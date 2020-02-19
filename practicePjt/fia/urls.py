from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.fia, name='fia'),
    path('<int:fiadetail_id>',views.fiadetail, name='fiadetail'),
    path('<int:fiadetail_id>/evaluate', views.fiaeval, name='fiaeval'),
    path('<int:fiadetail_id>/save', views.save, name='save'),
]