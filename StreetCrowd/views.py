from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def index(request):
    cars_list=[]
    context={'cars_list':cars_list}
    return render(request,'StreetCrowd/index.html',context)
