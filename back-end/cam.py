import base64
import urllib
import os
import random
import uuid
from datetime import datetime

import face_information

from flask import Flask, render_template, Response
import cv2
import numpy as np
from intrusionDetection import *

class VideoCamera(object):

    def __init__(self):
        #'rtmp://192.168.137.133:1935/live/home'
        self.cap = cv2.VideoCapture(0)
        self.detection = intrusionDetection()
        vw = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        vh = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        # fps = self.video .get(cv2.CAP_PROP_FPS)
        fileName = "D:/test/video/" + "-" + str(uuid.uuid4()) + ".mp4"
        print(str(datetime.now()))
        self.out = cv2.VideoWriter(fileName, cv2.CAP_ANY, int(self.cap.get(cv2.CAP_PROP_FOURCC)), 20,
                                   (int(vw), int(vh)), True)

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        success, image = self.cap.read()

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

        if not success:
            print('Cannot read video file')
            return
        else:
            # 判断是否有移动物体
            isMoving = self.detection.isHaveMovingObject(image)
            # 判断人脸识别是否需要报警
            isUnknowPeople = self.detection.face_classify(image)
            # 标记物体种类并判断是否有入侵到警戒区域
            isInvade = self.detection.imageClassification(image, x1, x2, y1, y2)
            # 如果有移动物体
            # if isMoving:
            # 如果有物体闯入警戒区域且人脸识别需要预警
            if isInvade and isUnknowPeople:
                # 录制视频
                if not self.out.isOpened():
                    vw = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
                    vh = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
                    fileName = "C:/Users/czh15/Desktop/demo/video/" + "-" + str(uuid.uuid4()) + ".mp4"
                    print(str(datetime.now()))
                    self.out = cv2.VideoWriter(fileName, cv2.CAP_ANY, int(self.cap.get(cv2.CAP_PROP_FOURCC)), 20,
                                               (int(vw), int(vh)), True)

                # image = self.detection.imageClassification(image)
                if self.out.isOpened():
                    self.out.write(image)
            else:
                if self.out.isOpened():
                    self.out.release()  #关闭视频保存

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def playback(camera):
    while True:
        success, image = camera.read()
        if not success:
            print('Cannot read video file')
            return
        ret, jpeg = cv2.imencode('.jpg', image)
        frame = jpeg.tobytes()
        # print('to bytes')
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def generate_random():
    a = 0
    str = ''
    while a < 4:
        b = random.randint(0, 9)
        tem = '%d' % b
        str += tem
        a += 1
    return str


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

    face_infor = face_information.faceTrain()
    faces, imageNums = face_infor.getImage("C:/Users/czh15/Desktop/demo/face/")
    face_infor.face_train(faces, imageNums)

    return tag