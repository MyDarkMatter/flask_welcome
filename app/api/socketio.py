import time

from flask_socketio import emit





# @socketio.on('my event')
# def handle_message(message):
#     print('received message: ' + message)
#
# @socketio.on('my event')
# def handle_my_custom_event(json):
#     print('received json: ' + str(json))
#     return 'success'
from hello import socketio


# @socketio.on('request_for_response',namespace='/testnamespace')
# def give_response(data):
#     value = data.get('param')
#     print(value)
#     #进行一些对value的处理或者其他操作,在此期间可以随时会调用emit方法向前台发送消息
#     emit('response',{'code':'200','msg':'start to process...'})
#
#     time.sleep(5)
#     emit('response',{'code':'200','msg':'processed'})

