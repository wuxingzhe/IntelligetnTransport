
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
from StreetCrowd.utils import handle_upload_file


def index(request):
    cars_list=[]
    context={'cars_list':cars_list}
    return render(request,'StreetCrowd/index.html',context)


def upload_data(request):
    """
    接收用户数据 view
    :param request:请求
    :return:
    """
    cars_list = []
    if request.method == "POST":
        files = request.FILES.getlist('file')
        handle_upload_file(files[0])
        # return HttpResponse('Successful')  # 此处简单返回一个成功的消息，在实际应用中可以返回到指定的页面中
    context = {'cars_list': cars_list}
    return render(request, 'StreetCrowd/index.html', context)
