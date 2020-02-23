from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .models import Evaluation
from .forms import *


# Create your views here.


<<<<<<< HEAD
# def tset(request):
#     form = SearchForm()
#     return render(request, "course.html", {"form": form})


# def fetch_course(request):
#     pass


# def fia(request):
#     fia_detail = lecture.objects
#     return render(request, "fia.html", {"fia_detail": fia_detail})


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
    # # new_eval.course = str(course.course_name)
    # new_eval.grade = request.GET["grade"]
    # new_eval.review = request.GET["review"]
    # new_eval.password = request.GET["password"]
    new_eval.save()
    return redirect("/course-evaluation/"+str(course.id))
    


# def save(request, fiadetail_id):
#     fia_detail = get_object_or_404(lecture, pk=fiadetail_id)
#     new_eval = evaluation()
#     new_eval.subject = fia_detail.name
#     new_eval.star = request.GET["star"]
#     new_eval.text = request.GET["written"]
#     new_eval.password = request.GET["password"]
#     new_eval.save()
#     return redirect("/fia/" + str(fia_detail.id))


# def delete_request(request, fiadetail_id, fiaeval_id):
#     fia_eval = get_object_or_404(evaluation, pk=fiaeval_id)
#     fia_detail = get_object_or_404(lecture, pk=fiadetail_id)
#     return render(
#         request, "deletePassword.html", {"fia_detail": fia_detail, "fia_eval": fia_eval}
#     )


# def delete(request, fiadetail_id, fiaeval_id):
#     fia_eval = get_object_or_404(evaluation, pk=fiaeval_id)
#     fia_detail = get_object_or_404(lecture, pk=fiadetail_id)
#     if fia_eval.password != int(request.GET["enteredPassword"]):
#         return render(
#             request,
#             "deletePassword.html",
#             {"fia_detail": fia_detail, "fia_eval": fia_eval},
#         )
#     fia_eval.delete()
#     return redirect("/fia/" + str(fia_detail.id))


# def update_request(request, fiadetail_id, fiaeval_id):
#     fia_eval = get_object_or_404(evaluation, pk=fiaeval_id)
#     fia_detail = get_object_or_404(lecture, pk=fiadetail_id)
#     return render(
#         request, "updatePassword.html", {"fia_detail": fia_detail, "fia_eval": fia_eval}
#     )


# def update(request, fiadetail_id, fiaeval_id):
#     fia_eval = get_object_or_404(evaluation, pk=fiaeval_id)
#     fia_detail = get_object_or_404(lecture, pk=fiadetail_id)
#     if fia_eval.password != int(request.GET["enteredPassword"]):
#         return render(
#             request,
#             "updatePassword.html",
#             {"fia_detail": fia_detail, "fia_eval": fia_eval},
#         )
#     return render(
#         request, "update.html", {"fia_detail": fia_detail, "fia_eval": fia_eval}
#     )
=======
def tset(request):

    form = SearchForm()
    return render(request, "course.html", {"form": form})
>>>>>>> 6fb1ada492fea3c4e62c8c6b6b84e8aed0e0b259


# def updateFinal(request, fiadetail_id, fiaeval_id):
#     fia_eval = get_object_or_404(evaluation, pk=fiaeval_id)
#     fia_detail = get_object_or_404(lecture, pk=fiadetail_id)
#     fia_eval.star = request.GET["star"]
#     fia_eval.text = request.GET["written"]
#     fia_eval.password = request.GET["password"]
#     fia_eval.save()
#     return redirect("/fia/" + str(fia_detail.id))
