import json
import os


from flask import request
from flask.json import jsonify
from flask_cors import cross_origin

from app.api import api
from app.forms.student import StudentForm
from app.model.base import db
from app.model.student import Student



#保存新生注册表单
@api.route('/v1/resgister',methods=['GET', 'POST'])
@cross_origin()
def register():
    born = request.form.get('born')
    data = request.form
    forms = StudentForm(request.form)

    if forms.validate():
        print('校验无误')
        with db.auto_commit():
            student = Student()
            student.set_attrs(forms.data)#处理映射关系
            db.session.add(student)
    else:
        print(forms.errors)
        return jsonify(forms.errors)

    return jsonify(status='success')




#照片上传
@api.route('/v1/fileup',methods=['GET', 'POST'])
@cross_origin()
def file_updata2():
    if request.method == "POST":
        file = request.files['file']
        file_name = file.filename
        file.save(os.path.join('app/templates', file_name))
        if file:
            return jsonify(status='success')
    return jsonify(status='fail')


#终极版本，同时获取数据和图片  可惜乱码没办法用
@api.route('/v2/fileup',methods=['GET', 'POST'])
@cross_origin()
def file_updata():
    if request.method == "POST":
        file = request.files.get("file")
        data = request.form.get('data')
        data = json.dumps(data)
        print(data)
        # if save_database(data) == 1000:
        #     return jsonify(status='file')
        file_name = file.filename
        file.save(os.path.join('app/templates', file_name))
        if file:
            return jsonify(status='success')
    return jsonify(status='file')


#数据交换测试实例
@api.route('/v1/test',methods=['GET', 'POST'])
@cross_origin()
def test():
    if request.method == "POST":
        first_name = request.form.get( "username", "null" )
        last_name = request.form.get( "password", "null" )
        print(first_name)


    return '133'

