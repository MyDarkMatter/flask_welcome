import cv2 as cv
import numpy as np

class VideoCamera():
    def __init__(self):
        # 通过opencv获取实时视频流
        self.video = cv.VideoCapture(0)
        self.face = 0

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # 因为opencv读取的图片并非jpeg格式，因此要用motion JPEG模式需要先将图片转码成jpg格式图片
        image = self.get_face(success,image)
        ret, jpeg = cv.imencode('.jpg', image)
        return jpeg.tobytes()


    def get_face(self,success,frame):

        #cap = cv.VideoCapture(0)  # 加载摄像头录制
        classifier = cv.CascadeClassifier(
            "D:/openCV/opencv-3.4.2/data/haarcascades/haarcascade_frontalface_default.xml")  # 加载模型

        while True:
            Precision = 2
            FaceFps = 1.12
            success, frame = success,frame
            frame = cv.flip(frame, 1)
            size = frame.shape[:2]
            image = np.zeros(size, dtype=np.float16)
            image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            cv.equalizeHist(image, image)  # 增强对比度
            divisor = 8
            h, w = size
            minSize = (w // divisor, h // divisor)
            faceRects = classifier.detectMultiScale(image, FaceFps, Precision, cv.CASCADE_SCALE_IMAGE, minSize)

            #print("检测结果", faceRects)
            if len(faceRects) > 0:
                self.face = 8899
                for faceRect in faceRects:
                    x, y, w, h = faceRect
                    cv.rectangle(frame, (x, y), (x + h, y + w), (0, 255, 0), 2)
                    cv.circle(frame, (x + w // 4, y + h // 4 + 30), min(w // 8, h // 8), (0, 0, 255))  # 左眼
                    cv.circle(frame, (x + 3 * w // 4, y + h // 4 + 30), min(w // 8, h // 8), (0, 0, 255))  # 右眼
                    cv.rectangle(frame, (x + 3 * w // 8, y + 3 * h // 4), (x + 5 * w // 8, y + 7 * h // 8),
                                  (0, 0, 255))  # 嘴巴
            else:
                Precision = 2  # 没有追踪到人脸降低精准度
                FaceFps = 1.3  # 加快帧率



            return frame