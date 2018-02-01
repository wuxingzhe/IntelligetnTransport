import os

from StreetCrowd.models import CarStatus


def handle_upload_file(file):
    path = 'datafile/uploads/'  # 上传文件的保存路径，可以自己指定任意的路径
    filename = file.name
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + filename, 'wb+')as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    with open(path + filename, 'r') as file:
        for line in file:
            line = line.split()
            if len(line):
                CarStatus.objects.create(car_id=int(line[0]), longitude=float(line[3]), latitude=float(line[4]),
                                         speed=int(line[6]), direction=int(line[8]), time=line[2])
