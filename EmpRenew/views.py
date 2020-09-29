from django.shortcuts import render
#from django.db import connection
from .models import Tdm0101Shain

# Create your views here.
#from django.http import HttpResponse

def edit(request):
    return render(request, 'EmpRenew/edit.html', {})
def disp(request):
#    cursor = connection.cursor()
#    cursor.execute('SELECT tdm0101_shain_cd, tdm0101_shain_nm, tdm0101_shain_nm_k FROM tdm0101_shain')
#    display = cursor.fetchall()
#    display = Tdm0101Shain.objects.get(tdm0101_shain_cd='002714')
    display = Tdm0101Shain.objects.raw('select * from TDM0101_SHAIN where tdm0101_shain_cd=002714')
    return render(request, 'EmpRenew/disp.html', {'display':display})
