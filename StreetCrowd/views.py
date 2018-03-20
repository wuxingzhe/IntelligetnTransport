
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

from .models import CarStatus, PointsPrediction
import json
# Create your views here.
from StreetCrowd.utils import handle_upload_file, handleFileThread


def index(request):
    cars_list=[]
    time_id=[]
    car_id=[]
    cars=CarStatus.objects.order_by("timeID","car_id").all()
    points=PointsPrediction.objects.order_by("frame_id", "coord_id").all()
    lines=LinesPrediction.objects.all()

    print(len(points))
    points_list=[]
    frame_id=[]
    coord_id=[]
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
        car_id.append(p.car_id)

    for p in points:
        frame_id.append(p.frame_id)
        coord_id.append(p.coord_id)
        tmp=[]
        tmp.append(p.longitude)
        tmp.append(p.latitude)
        tmp.append(p.virsual_val)
        points_list.append(tmp)
    print(points_list)

    lines_list=[]
    lines_frame_id=[]
    lines_coord_id=[]
    for p in lines:
        lines_list.append([[p.start_longitude,p.start_latitude],[p.end_longitude,p.end_latitude]])
        lines_frame_id.append(p.frame_id)
        lines_coord_id.append(p.coord_id)

    context={'cars_list':json.dumps(cars_list) ,'time_id':json.dumps(time_id),'car_id':json.dumps(car_id),'points_list':json.dumps(points_list),'frame_id':json.dumps(frame_id),'coord_id':json.dumps(coord_id),'lines_list':json.dumps(lines_list),'lines_frame_id':json.dumps(lines_frame_id),'lines_coord_id':json.dumps(lines_coord_id)}
    # context ={}
    return render(request,'StreetCrowd/index.html',context)


def upload_data(request):
    """
    接收用户数据 view
    :param request:请求
    :return:
    """
    if request.method == "POST":
        files = request.FILES.getlist('file')
        # print(request.FILES.getlist('file'))
        # print(request.FILES.getlist('form'))
        filepath=handle_upload_file(files[0])
        file_thread = handleFileThread(1,filepath)
        file_thread.start()
        # file_thread.join()
        # return HttpResponse('Successful')  # 此处简单返回一个成功的消息，在实际应用中可以返回到指定的页面中
    name_dict = {"resultCode":200}
    return JsonResponse(name_dict)
    # return redirect('/StreetCrowd')