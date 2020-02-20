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
    new_eval.password = request.GET['password']
    new_eval.save()
    return redirect('/fia/'+str(fia_detail.id))

def delete_request(request, fiadetail_id, fiaeval_id):
    fia_eval = get_object_or_404(evaluation, pk=fiaeval_id)
    fia_detail = get_object_or_404(lecture, pk=fiadetail_id)
    return render(request, 'deletePassword.html', {'fia_detail':fia_detail, 'fia_eval':fia_eval})

def delete(request, fiadetail_id, fiaeval_id):
    fia_eval = get_object_or_404(evaluation, pk=fiaeval_id)
    fia_detail = get_object_or_404(lecture, pk=fiadetail_id) 
    if fia_eval.password != int(request.GET['enteredPassword']):   
        return render(request, 'deletePassword.html', {'fia_detail':fia_detail, 'fia_eval':fia_eval})
    fia_eval.delete()
    return redirect('/fia/'+str(fia_detail.id))

def update_request(request, fiadetail_id, fiaeval_id):
    fia_eval = get_object_or_404(evaluation, pk=fiaeval_id)
    fia_detail = get_object_or_404(lecture, pk=fiadetail_id)
    return render(request, 'updatePassword.html', {'fia_detail':fia_detail, 'fia_eval':fia_eval})

def update(request, fiadetail_id, fiaeval_id):
    fia_eval = get_object_or_404(evaluation, pk=fiaeval_id)
    fia_detail = get_object_or_404(lecture, pk=fiadetail_id)
    if fia_eval.password != int(request.GET['enteredPassword']):   
        return render(request, 'updatePassword.html', {'fia_detail':fia_detail, 'fia_eval':fia_eval})
    return render(request, 'update.html', {'fia_detail':fia_detail, 'fia_eval':fia_eval})

def updateFinal(request, fiadetail_id, fiaeval_id):
    fia_eval = get_object_or_404(evaluation, pk=fiaeval_id)
    fia_detail = get_object_or_404(lecture, pk=fiadetail_id)
    fia_eval.star = request.GET['star']
    fia_eval.text = request.GET['written']
    fia_eval.password = request.GET['password']
    fia_eval.save()
    return redirect('/fia/'+str(fia_detail.id))