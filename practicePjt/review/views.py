from django.shortcuts import render
from courses.models import Courses

# Create your views here.
def home(request):
    courses = Courses.objects
    return render(request, 'home.html', {'courses':courses})
