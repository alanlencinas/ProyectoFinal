from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.views import obtenerAvatar



def inicio1(request):
    return render(request, 'MiBlog/blog.html', {"avatar": obtenerAvatar(request)})

def perfumeriadetalle(request):
    return render(request, "MiBlog/perfumeriadetalle.html", {"avatar": obtenerAvatar(request)})
