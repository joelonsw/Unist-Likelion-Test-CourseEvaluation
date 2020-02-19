from django.shortcuts import render,get_object_or_404, redirect
from .models import lecture
from .models import evaluation

# Create your views here.
def fia(request):
    fia_detail = lecture.objects
    return render(request, 'fia.html', {'fia_detail':fia_detail})

def fiadetail(request, fiadetail_id):
    fia_detail = get_object_or_404(lecture, pk=fiadetail_id)
    fia_eval = evaluation.objects
    return render(request, 'fiadetail.html', {'fia_detail':fia_detail, 'fia_eval':fia_eval})

def fiaeval(request, fiadetail_id):
    fia_detail = get_object_or_404(lecture, pk=fiadetail_id)
    return render(request, 'fiaeval.html', {'fia_detail':fia_detail})

def save(request,fiadetail_id):
    fia_detail = get_object_or_404(lecture, pk=fiadetail_id)
    new_eval = evaluation()
    new_eval.subject = fia_detail.name
    new_eval.star = request.GET['star']
    new_eval.text = request.GET['written']
    new_eval.save()
    return redirect('/fia/'+str(fia_detail.id))