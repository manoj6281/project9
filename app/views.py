from django.shortcuts import render

# Create your views here.


def conditions(request):
    d={'a':10,'b':5}
    return render(request,'conditions.html',d)