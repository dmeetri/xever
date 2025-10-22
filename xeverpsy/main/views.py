from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def works(request):
    return render(request, 'main/works.html')