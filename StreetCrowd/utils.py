import os
import threading

from StreetCrowd.models import CarStatus, PointsPrediction, LinesPrediction
from django.db import transaction


class handleFileThread(threading.Thread):
    def __init__(self,threadID,filepath):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.filepath = filepath

    def run(self):
        filename = self.filepath.split('/')[-1]
        if filename == 'point.csv':
            # threadLock = threading.Lock()
            # threadLock.acquire()
            cnt = 0
            try:
                with transaction.atomic():
                    PointsPrediction.objects.all().delete()
                    with open(self.filepath, 'r') as file:
                        for line in file:
                            cnt += 1
                            line = line[:-1].split(',')
                            if len(line) > 0:

                                PointsPrediction.objects.create(longitude=float(line[0]),
                                                         latitude=float(line[1]),
                                                        virsual_val=int(line[2]), frame_id=int(line[3]),coord_id = int(line[-1]))
                            print(line)
                            if (cnt % 50 == 0):
                                print("%d data inserted" % (cnt))
                        print("insertion complete")
                        # PointsPrediction.objects.all().order_by("frame_id", "coord_id")
                        print("The size of PointsPrediction table: ", len(PointsPrediction.objects.all()))
            except Exception as e:
                print(e)
            print("The size of PointsPrediction table: ", len(PointsPrediction.objects.all()))
        elif filename == 'lines.csv':
            # threadLock = threading.Lock()
            # threadLock.acquire()
            cnt = 0
            try:
                with transaction.atomic():
                    LinesPrediction.objects.all().delete()
                    with open(self.filepath, 'r') as file:
                        for line in file:
                            cnt += 1
                            line = line[:-1].split(',')
                            if len(line) > 0:
                                LinesPrediction.objects.create(start_longitude=float(line[0]),
                                                               start_latitude=float(line[1]),end_longitude=float(line[2]),
                                                               end_latitude=float(line[3]),
                                                        frame_id=int(line[4]),coord_id = int(line[5]))
                            print(line)
                            if (cnt % 50 == 0):
                                print("%d data inserted" % (cnt))
                        print("insertion complete")
                        # PointsPrediction.objects.all().order_by("frame_id", "coord_id")
                        print("The size of LinesPrediction table: ", len(LinesPrediction.objects.all()))
            except Exception as e:
                print(e)
        else:
            # threadLock = threading.Lock()
            # threadLock.acquire()
            cnt = 0
            try:
                with transaction.atomic():
                    CarStatus.objects.all().delete()
                    with open(self.filepath, 'r') as file:
                        for line in file:
                            cnt+=1
                            line = line.split()
                            if len(line)>0:
                                CarStatus.objects.create(car_id=int(line[0]), longitude=float(line[3]), latitude=float(line[4]),
                                                         speed=float(line[6]),timeID=int(line[-1]))
                            if(cnt%50==0):
                                print("%d data inserted"%(cnt))
                        print("insertion complete")
                        CarStatus.objects.all().order_by("timeID","car_id")
                        print("The size of Carstatus table: ",len(CarStatus.objects.all()))
            except Exception:
                print(Exception)
            # threadLock.release()

def handle_upload_file(file):
    path = 'datafile/uploads/'  # 上传文件的保存路径，可以自己指定任意的路径
    filename = file.name
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + filename, 'wb+')as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return path+filename
