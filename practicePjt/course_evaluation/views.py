from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .models import Course, Evaluation
from .serializers import CourseSerializer, EvluationSerializer


def home(request):
    return render(request, "course.html")


@api_view(["POST"])
@permission_classes([AllowAny])
def search_course(request):
    course_code = request.data.get("course_code", "")
    course_name = request.data.get("course_name", "")
    course_professor = request.data.get("course_professor", "")
    course_semester = request.data.get("course_semester", "")

    course = Course.objects.all()
    if course_code != "":
        course = course.filter(course_code__contains=course_code)
    if course_name != "":
        course = course.filter(course_name__contains=course_name)
    if course_professor != "":
        course = course.filter(course_professor__contains=course_professor)
    if course_semester != "":
        course = course.filter(course_semester__contains=course_semester)
    course = CourseSerializer(course, many=True).data

    # return render(request, "course.html", {"course": course})
    return Response(course, status=200)


@api_view(["POST"])
@permission_classes([AllowAny])
def create_course_evaluation(request, course_id):
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({"message": "no such objects"}, status=404)

    review = request.data.get("review", "")
    grade = request.data.get("grade", 3)
    password = int(request.data.get("password", 0000))

    evaluation = Evaluation.objects.create(
        course=course, grade=grade, review=review, password=password
    )

    evaluation = EvluationSerializer(evaluation).data
    return Response(evaluation, status=200)


@api_view(["GET"])
@permission_classes([AllowAny])
def fetch_course_evaluation(request, course_id):
    course_id = request.GET.get("course_id")
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({"message": "no such objects"}, status=404)
    evaluation = Evaluation.objects.filter(course=course_id)
    return render(request, "detail.html", {"course": course, "evaluation": evaluation})


def detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    evaluation = Evaluation.objects.filter(course=course_id)
    return render(request, "detail.html", {"course": course, "evaluation": evaluation})


def evaluation(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, "evaluation_form.html", {"course": course})


def save(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    new_eval = Evaluation.objects.create(
        course=course,
        grade=request.GET["grade"],
        review=request.GET["review"],
        password=request.GET["password"],
    )
    new_eval.save()
    return redirect("/course-evaluation/" + str(course.id))


def delete_request(request, eval_id):
    evaluation = get_object_or_404(Evaluation, pk=eval_id)
    msg = "Delete"
    return render(request, "Password.html", {"evaluation": evaluation, "delete": msg})


def delete(request, eval_id):
    evaluation = get_object_or_404(Evaluation, pk=eval_id)
    if evaluation.password != int(request.GET["enteredPassword"]):
        return render(request, "Password.html", {"evaluation": evaluation},)
    evaluation.delete()
    return redirect("/course-evaluation/" + str(evaluation.course.id))


def update_request(request, eval_id):
    evaluation = get_object_or_404(Evaluation, pk=eval_id)
    msg = "Update"
    return render(request, "Password.html", {"evaluation": evaluation, "update": msg})


def update(request, eval_id):
    evaluation = get_object_or_404(Evaluation, pk=eval_id)
    msg = "update"
    if evaluation.password != int(request.GET["enteredPassword"]):
        return render(request, "Password.html", {"evaluation": evaluation},)
    return render(
        request, "evaluation_form.html", {"evaluation": evaluation, "update": msg}
    )


def update_final(request, eval_id):
    evaluation = get_object_or_404(Evaluation, pk=eval_id)
    evaluation.grade = request.GET["grade"]
    evaluation.review = request.GET["review"]
    evaluation.password = request.GET["password"]
    evaluation.save()
    return redirect("/course-evaluation/" + str(evaluation.course.id))
