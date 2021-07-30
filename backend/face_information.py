import sys
import numpy as np
from PIL import Image
import os
import cv2


class faceTrain(object):
    def __init__(self):
        # 人脸数据路径
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        # 使用opencv预置人脸检测的模型
        self.face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')

    def getImage(self, path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]  # 读取照片素材所有文件路径
        faceSamples = []
        imageNums = []
        for imagePath in imagePaths:
            # print(imagePath)
            # print(type(imagePath))
            PIL_img = Image.open(imagePath).convert('L')  # 转成灰度图

            img_numpy = np.array(PIL_img, 'uint8')
            imageNum = int(os.path.split(imagePath)[-1].split(".")[1])
            # print(imageNum)
            faces = self.face_classifier.detectMultiScale(img_numpy)
            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y + h, x: x + w])
                imageNums.append(imageNum)
        return faceSamples, imageNums, imagePaths

    def face_train(self, faces, imageNums):
        self.recognizer.train(faces, np.array(imageNums))   #训练
        self.recognizer.write(r'C:/Users/czh15/Desktop/demo/face_trainer/trainer.yml')
        print("{0} faces trained. Exiting Program".format(len(imageNums)))
