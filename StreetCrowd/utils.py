import os
import threading

from StreetCrowd.models import CarStatus


class handleFileThread(threading.Thread):
    def __init__(self,threadID,filepath):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.filepath = filepath
    def run(self):
        threadLock = threading.Lock()
        # threadLock.acquire()
        cnt = 0
        try:
            with open(self.filepath, 'r') as file:
                for line in file:
                    cnt+=1
                    line = line.split()
                    if len(line):
                        CarStatus.objects.create(car_id=int(line[0]), longitude=float(line[3]), latitude=float(line[4]),
                                                 speed=int(line[6]), direction=int(line[8]), time=line[2])
                    if(cnt%50==0):
                        print("%d data inserted"%(cnt))
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
