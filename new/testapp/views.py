from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

#function based
from django.http import HttpResponse
def home(request):
    # return HttpResponse("welcome")
    context={'name':'arun','age':24}
    return render(request,'home.html',context)

def index(request):
    # return HttpResponse("Django")
    return render(request,'base.html')