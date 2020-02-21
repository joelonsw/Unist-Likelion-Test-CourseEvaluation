from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import *

# Register your models here.


@admin.register(lecture, evaluation, Course)
class ImportExport(ImportExportActionModelAdmin):
    pass