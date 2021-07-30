from flask import Flask, render_template, Response
import cv2
import numpy as np
from flask_cors import CORS

from intrusionDetection import *


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
class playbackCamera(object):

    def __init__(self, filename):
        self.cap = cv2.VideoCapture(filename)

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        success, image = self.cap.read()
        if not success:
            print("not success")
            return
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


def gen_playback(camera):
    while True:
        frame = camera.get_frame()
        if frame == None:
            del camera
            return
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

