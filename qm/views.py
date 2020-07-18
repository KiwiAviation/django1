from django.shortcuts import render
from django.http import HttpResponse

def qm(request):
    # return HttpResponse('<h1>Quartermaster</h1>')
    return render(request, 'qm/quartermaster.html')
