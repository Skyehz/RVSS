import base64
import random
import os
from datetime import datetime
import uuid
from numpy import unicode

import face_information
from intrusionDetection import *
from login.sqltest import add_invade_info
import _thread
import time

# 为线程定义一个函数
def add_invade(time, location, remark, filename):
    # 在数据库中添加入侵信息
    add_invade_info(time, location, remark, filename)

class VideoCamera(object):

    def __init__(self):
        self.cap = cv2.VideoCapture('rtmp://192.168.43.217:1935/live/home')
        # self.cap = cv2.VideoCapture(0)
        self.detection = intrusionDetection()
        self.start_time = datetime.now()
        time = self.start_time.strftime('%Y-%m-%d')
        vw = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        vh = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        hour = self.start_time.hour
        minute = self.start_time.minute
        second = self.start_time.second
        time2 = str(hour) + "-" + str(minute) + "-" + str(second)

        fileName = "C:/Users/czh15/Desktop/demo/video/" + time + "-" + time2 + ".mp4"
        print(str(datetime.now()))
        self.out = cv2.VideoWriter(fileName, cv2.CAP_ANY, int(self.cap.get(cv2.CAP_PROP_FOURCC)), 10,
                                   (int(vw), int(vh)), True)
        self.out.release()
        os.remove(fileName)

    def __del__(self):
        self.cap.release()


    def get_frame(self):
        success, image = self.cap.read()
        datet = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        cv2.putText(image, datet, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255), 2, cv2.LINE_AA)  # cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, 8

        # 画出警戒区域
        area = area_find()
        if area[0][0] < area[1][0]:
            x1 = area[0][0]
            x2 = area[1][0]
        else:
            x2 = area[0][0]
            x1 = area[1][0]
        if area[0][1] < area[1][1]:
            y1 = area[0][1]
            y2 = area[1][1]
        else:
            y2 = area[0][1]
            y1 = area[1][1]
        ptLeftTop = (x1, y1)
        ptRightBottom = (x2, y2)
        cv2.rectangle(image, ptLeftTop, ptRightBottom, (255, 0, 0), 2)

        success = True
        if not success:
            print('Cannot read video file')
            return
        else:
            # 标记物体种类并判断是否有入侵到警戒区域
            isInvade = self.detection.imageClassification(image, x1, x2, y1, y2)
            # 判断人脸识别是否需要报警
            isUnknowPeople = self.detection.face_classify(image)

            # 如果有物体闯入警戒区域且人脸识别需要预警
            if isInvade and isUnknowPeople:
                # 录制视频
                if not self.out.isOpened():
                    self.start_time = datetime.now()
                    time = self.start_time.strftime('%Y-%m-%d')
                    vw = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
                    vh = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
                    hour = self.start_time.hour
                    minute = self.start_time.minute
                    second = self.start_time.second
                    time2 = str(hour) + "-" + str(minute) + "-" + str(second)
                    fileName = "C:/Users/czh15/Desktop/demo/video/" + time + "-" + time2 + ".mp4"
                    self.out = cv2.VideoWriter(fileName, cv2.CAP_ANY, int(self.cap.get(cv2.CAP_PROP_FOURCC)), 10,
                                               (int(vw), int(vh)), True)

                    # 创建线程，在数据库中添加信息
                    try:
                        _thread.start_new_thread(add_invade, (self.start_time.strftime('%Y-%m-%d %H:%M:%S'), 'warehouse', 'invade',fileName))
                    except:
                        print("Error: 无法启动线程")
                # image = self.detection.imageClassification(image)
                if self.out.isOpened():
                    self.out.write(image)
            else:
                if self.out.isOpened() and (datetime.now()-self.start_time).seconds<10:
                    self.out.write(image)
                if self.out.isOpened() and (datetime.now()-self.start_time).seconds>10:
                    self.out.release()  #关闭视频保存


        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# def playback(camera):
#     while True:
#         success, image = camera.read()
#         if not success:
#             print('Cannot read video file')
#             return
#         ret, jpeg = cv2.imencode('.jpg', image)
#         frame = jpeg.tobytes()
#         # print('to bytes')
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def generate_random():
    a = 0
    str = ''
    while a < 4:
        b = random.randint(0, 9)
        tem = '%d' % b
        str += tem
        a += 1
    return str


def train_face(file_path):
    face_infor = face_information.faceTrain()
    faces, imageNums ,imagePaths= face_infor.getImage(file_path)
    face_infor.face_train(faces, imageNums)


def add_face(imgcode):
    n = 0
    file_path = 'C:/Users/czh15/Desktop/demo/face/'
    tag = generate_random()
    while n < 100:
        code = imgcode[n][22:len(imgcode[n])]
        imgdata = base64.b64decode(code)
        # print('\n\n\n\n', code)
        file_name = "#."+tag+"." + str(uuid.uuid4())+'.jpg'
        file = open(file_name, 'wb')
        file.write(imgdata)
        file.close()

        try:
            img = cv2.imread(file_name, 1)
            cv2.imwrite(os.path.join(file_path, file_name), img)
            cv2.waitKey(0)
        except IOError as e:
            print("IOError")
        except Exception as e:
            print("Exception")

        n += 1

    try:
        _thread.start_new_thread(train_face, (file_path,))
    except:
        print("Error: 无法启动线程")

    return tag