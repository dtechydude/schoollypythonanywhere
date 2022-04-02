from django.conf import settings
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.urls import reverse_lazy
from results.forms import PrintResultForm, ResultUploadForm
from django.contrib import messages
from results.models import PrintResult, Result
import os

# Create your views here.

@login_required
def printresult(request):
    result = PrintResult.objects.all()
    context = {
        'result':result
    }
    
    return render(request, 'results/view_result.html', context)





@login_required
def printresultform(request):
    if request.method == 'POST':
        print_form = PrintResult(request.POST)
                
        if print_form.is_valid():
             print_form.save()
             messages.success(request, f'The Result has been uploaded successfully')
             return HttpResponseRedirect (request, 'students/studentpage')
        
    else:
        print_form = PrintResultForm()
    
        file = PrintResult.objects.all()
        # 'print_form': print_form
   
    return render(request, 'results/print_resultform.html', {'print_form': print_form, 'file':file })





@login_required
def uploadresult(request):
    if request.method == 'POST':
        upload_form = ResultUploadForm(request.POST)
                
        if upload_form.is_valid():
             upload_form.save()
             messages.success(request, f'The Result has been uploaded successfully')
             return redirect('studentpage')
        
    else:
        upload_form = ResultUploadForm()

    return render(request, 'results/result_entry_form.html', {'upload_form': upload_form})

# FUNCTION FOR DOWNLOADING FILE
def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application/file")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response

    raise Http404



@login_required
def view_self_result(request):
    myresult = PrintResult.objects.filter(user=request.user)
    context = {
        'myresult':myresult
    }
    
    return render(request, 'results/view_self_result.html', context)

# FUNCTION FOR DOWNLOADING FILE
def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application/file")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response

    raise Http404

