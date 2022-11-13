from django.shortcuts import render
from django.db.models import Q
from .models import Correspondencia

def correspondencia(request):
    residencia_query = request.GET.get('residencia_info')
    correspondencias = Correspondencia.objects.all()
    
    if residencia_query:
        correspondencias = Correspondencia.objects.filter(Q(residencia__icontains = residencia_query))
    
    return render(request,'Core/correspondencia.html',{'correspondencias':correspondencias})

def inicio(request):
    return render(request,'Core/inicio.html',{})

