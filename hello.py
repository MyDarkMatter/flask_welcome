import time
from threading import Lock
import psutil as psutil
from flask_socketio import SocketIO, emit
from app import create_app

app = create_app()
socketio = SocketIO(app)#初始化socketio核心
thread = None
thread_lock = Lock()

#处理数据返回接口
def give_database_response():
    while True:
        socketio.sleep(2)
        #进行一些对value的处理或者其他操作,在此期间可以随时会调用emit方法向前台发送消息
        socketio.emit('response_data',{'code':'200','msg':'connect'},namespace='/request_response')




#接收客户端信息(处理视频流接口)
@socketio.on('my video',namespace='/request_response')
def handle_my_video_event(json):
    print('received json: ' + str(json))


@socketio.on('connect', namespace='/request_response')
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=give_database_response)



#错误返回
@socketio.on_error()
def error_handler(e):
    emit('response', {'code': '500', 'msg': e})
    print(e)

if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0',port=81)