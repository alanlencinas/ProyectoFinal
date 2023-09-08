from django.shortcuts import render
from django.http import HttpResponse



def inicio1(request):
    return render(request, 'MiBlog/blog.html')


