from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse

def list(request):
     return render(request, 'EmpRenew/edit.html', {})
def printout(request):
     return render(request, 'EmpRenew/disp.html', {})
