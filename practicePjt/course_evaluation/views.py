from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .models import Evaluation
from .forms import *
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import CourseSerializer

def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    evaluation = Evaluation.objects.filter(course=course_id)
    return render(
        request, "detail.html", {"course":course , "evaluation":evaluation}
    )


def evaluation(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, "evaluation_form.html", {"course": course})

def save(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    new_eval = Evaluation.objects.create(course=course, grade=request.GET["grade"], review=request.GET["review"], password= request.GET["password"])
    new_eval.save()
    return redirect("/course-evaluation/"+str(course.id))
    

def delete_request(request, eval_id):
    evaluation = get_object_or_404(Evaluation, pk=eval_id)
    msg = 'Delete'
    return render( request, "Password.html", {"evaluation":evaluation, 'delete':msg} )

def delete(request, eval_id):
    evaluation = get_object_or_404(Evaluation, pk=eval_id)
    if evaluation.password != int(request.GET["enteredPassword"]):
        return render(
            request,
            "Password.html",
            {"evaluation":evaluation},
        )
    evaluation.delete()
    return redirect("/course-evaluation/" + str(evaluation.course.id))


def update_request(request, eval_id):
    evaluation = get_object_or_404(Evaluation, pk=eval_id)
    msg = 'Update'
    return render(
        request, "Password.html", {"evaluation":evaluation , "update":msg}
    )


def update(request, eval_id):
    evaluation = get_object_or_404(Evaluation, pk=eval_id)
    msg = 'update'
    if evaluation.password != int(request.GET["enteredPassword"]):
        return render(
            request,
            "Password.html",
            {"evaluation": evaluation},
        )
    return render(request, "evaluation_form.html", {"evaluation": evaluation, "update":msg})


def update_final(request, eval_id):
    evaluation = get_object_or_404(Evaluation, pk=eval_id)
    evaluation.grade = request.GET["grade"]
    evaluation.review = request.GET["review"]
    evaluation.password = request.GET["password"]
    evaluation.save()
    return redirect("/course-evaluation/" + str(evaluation.course.id))
