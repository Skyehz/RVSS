import os
import uuid
import cv2
from cv2 import getStructuringElement

from login.sqltest import area_find, face_find


class intrusionDetection(object):
    # 初始化
    def __init__(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read('C:/Users/czh15/Desktop/demo/face_trainer/trainer.yml')

        # 类别信息
        self.objName = ["background",
                        "aeroplane", "bicycle", "bird", "boat",
                        "bottle", "bus", "car", "cat", "chair",
                        "cow", "diningtable", "dog", "horse",
                        "motorbike", "person", "pottedplant",
                        "sheep", "sofa", "train", "tvmonitor"]

        # 模型路径 需要下载模型文件
        model_bin = "C:/Users/czh15/Desktop/ssd/MobileNetSSD_deploy.caffemodel"
        config_text = "C:/Users/czh15/Desktop/ssd/MobileNetSSD_deploy.prototxt"

        # 加载模型
        self.net = cv2.dnn.readNetFromCaffe(config_text, model_bin)
        # 使用opencv预置人脸检测的模型
        self.face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
        self.fgbg = cv2.createBackgroundSubtractorMOG2()
        self.kernel = getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # 判断是否有移动物体
    def isHaveMovingObject(self, image):

        fgmask = self.fgbg.apply(image)
        dilate = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, self.kernel)
        cnts, hierarchy = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]

        for c in cnts:
            if cv2.contourArea(c) < 500:  # 计算轮廓面积
                continue
            return True
        return False

    # 目标检测物体分类
    def imageClassification(self, image,  x1, x2, y1, y2):

        (H, W) = image.shape[:2]

        blobImage = cv2.dnn.blobFromImage(image, 0.007843, (300, 300), (127.5, 127.5, 127.5), True, False)
        self.net.setInput(blobImage)
        cvOut = self.net.forward()
        pl = pt = pr = pb = 0
        flag = False
        for detection in cvOut[0, 0, :, :]:
            score = float(detection[2])
            objIndex = int(detection[1])  # 已获取识别的物体类别
            if score > 0.6:
                left = detection[3] * W
                top = detection[4] * H
                right = detection[5] * W
                bottom = detection[6] * H

                pl = int(left)
                pt = int(top)
                pr = int(right)
                pb = int(bottom)

                # 绘制,测试到有入侵画红框，无入侵画绿框
                # 无入侵（绿）
                # if pb<y1 or pt>y2 or pr<x1 or pl>x2:
                if pt >y1:
                    # 画框标注物体种类
                    cv2.rectangle(image, (int(left), int(top)), (int(right), int(bottom)), (0, 255, 0), thickness=2)
                    cv2.putText(image, "score:%.2f, %s" % (score, self.objName[objIndex]),
                                (int(left) - 10, int(top) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, 8)
                # 有入侵（红）
                else:
                    cv2.rectangle(image, (int(left), int(top)), (int(right), int(bottom)), (0, 0, 255), thickness=2)
                    cv2.putText(image, "score:%.2f, %s" % (score, self.objName[objIndex]),
                                (int(left) - 10, int(top) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, 8)
                    cv2.putText(image, "Invade!!!!",
                                (int(left) - 50, int(top) - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, 8)
                    flag = True
        return flag
        # return image

    # 判断人脸识别是否需要报警
    def face_classify(self, image):
        # 将原图画转换为灰阶图像
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        flag = True
        # 人脸识别
        face = self.face_classifier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=2, minSize=(24, 24))
        for (x, y, w, h) in face:
            idnum, confidence = self.recognizer.predict(gray[y:y + h, x:x + w])
            if confidence < 68:  # 如果置信度小于68则说明该人有很大可能是本人
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                name = face_find(idnum)
                confidence = "{0}%".format(round(100 - confidence))
                flag = False
            else:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                name = "unknown"
                confidence = "{0}%".format(round(100 - confidence))
            cv2.putText(image, name, (x + 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
            cv2.putText(image, str(confidence), (x + 5, y + h - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

        # 若识别到人脸且认识,返回false(不用报警)；若识别未到人脸或识别到但不认识，返回true（用报警）
        return flag

    # 判断是否闯入入侵区域
    # def isInvade(self, image):
    #     (H, W) = image.shape[:2]
    #     blobImage = cv2.dnn.blobFromImage(image, 0.007843, (300, 300), (127.5, 127.5, 127.5), True, False)
    #     self.net.setInput(blobImage)
    #     cvOut = self.net.forward()
    #     pl = pt = pr = pb = 0
    #     for detection in cvOut[0, 0, :, :]:
    #         score = float(detection[2])
    #         objIndex = int(detection[1])  # 已获取识别的物体类别
    #         if score > 0.6:
    #             left = detection[3] * W
    #             top = detection[4] * H
    #             right = detection[5] * W
    #             bottom = detection[6] * H
    #
    #             pl = int(left)
    #             pt = int(top)
    #             pr = int(right)
    #             pb = int(bottom)
    #
    #
    #     return False

    # 获取名字
    def findName(self, path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]  # 读取照片素材所有文件路径
        names = []
        for imagePath in imagePaths:
            name = os.path.split(imagePath)[-1].split("#")[1]
            if name in names:
                continue
            else:
                names.append(name)
        return names

