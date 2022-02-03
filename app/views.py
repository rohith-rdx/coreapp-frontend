from django.http import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def dashboard(request):
    return render(request,'dashboard.html')

def task(request):
    return render(request,'task.html')
def project(request):
    return render(request,'project.html')
def projectdetails(request):
    return render(request,'projectdetails.html')
def assigned(request):
    return render(request,'assigned.html')
def submitted(request):
    return render(request,'submitted.html')