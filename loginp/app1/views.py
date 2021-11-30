from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'app1.html',{'titles':'AJIT'})

def profile(request):
    return HttpResponse('welcome ajit')
def expression(request):
    a = int(request.POST['text1'])
    b = int(request.POST['text2'])
    c = (a+b)**2
    return render(request,'output.html',{'result':c})