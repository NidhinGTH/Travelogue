from django.shortcuts import render
from app1.models import Place,Team
# Create your views here.
def home(request):
    p=Place.objects.all()
    q = Team.objects.all()
    return render(request,'home.html',{'p':p,'q':q})

