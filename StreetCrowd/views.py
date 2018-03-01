
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import CarStatus
import json
# Create your views here.
from StreetCrowd.utils import handle_upload_file, handleFileThread


def index(request):
    cars_list=[]
    time_id=[]
    cars=CarStatus.objects.all().order_by("timeID","car_id")
    for p in cars:
        tmp=[]
        tmp.append(p.longitude)
        tmp.append(p.latitude)
        num=(100-p.speed)*(100-p.speed)*1.0/100
        if num<20:
            num=60
        elif num<40:
            num=120
        tmp.append(num)
        cars_list.append(tmp)
        time_id.append(p.timeID)
    context={'cars_list':json.dumps(cars_list) ,'time_id':json.dumps(time_id)}
    return render(request,'StreetCrowd/index.html',context)


def upload_data(request):
    """
    接收用户数据 view
    :param request:请求
    :return:
    """
    if request.method == "POST":
        files = request.FILES.getlist('file')
        filepath=handle_upload_file(files[0])
        file_thread = handleFileThread(1,filepath)
        file_thread.start()
        # return HttpResponse('Successful')  # 此处简单返回一个成功的消息，在实际应用中可以返回到指定的页面中
    return redirect('/StreetCrowd')
