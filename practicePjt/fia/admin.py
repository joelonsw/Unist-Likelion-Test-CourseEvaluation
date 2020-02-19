from django.contrib import admin
from .models import lecture
from .models import evaluation
# Register your models here.

admin.site.register(lecture)
admin.site.register(evaluation)