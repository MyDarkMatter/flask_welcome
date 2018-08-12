from flask import render_template, Response
from app.model.video import VideoCamera
from app.api import api

@api.route('/video_feed')  # 这个地址返回视频流响应
def video_feed():

    return Response(gen(VideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')


def gen(camera):
    while True:
        frame = camera.get_frame()
        face = camera.face
        print(camera.face)
        # 使用generator函数输出视频流， 每次请求输出的content类型是image/jpeg
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


