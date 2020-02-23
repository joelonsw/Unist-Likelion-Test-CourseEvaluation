from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from fia.models import Course
from .serializers import CourseSerializer

# Create your views here.


@api_view(["POST"])
@permission_classes([AllowAny])
def tset(request):
    course_code = request.data.get("course_code", "")
    course_name = request.data.get("course_name", "")
    course_professor = request.data.get("course_professor", "")
    course_semester = request.data.get("course_semester", "")

    course = Course.objects.all()
    if course_name != "":
        course = course.filter(course_name=course_name)

    course = CourseSerializer(course, many=True).data

    # return render(request, "course.html", {"data": data})
    return Response(course, status=200)

