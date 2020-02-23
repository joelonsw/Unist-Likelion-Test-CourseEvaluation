from django.shortcuts import render
from .forms import SearchForm

# Create your views here.


def tset(request):

    form = SearchForm()
    return render(request, "course.html", {"form": form})


def fetch_course(request):
    pass
