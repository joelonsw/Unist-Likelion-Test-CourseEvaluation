from django.shortcuts import render
from fia.models import Course

# Create your views here.
def home(request):
    courses = Course.objects
    return render(request, 'home.html', {'courses': courses})
