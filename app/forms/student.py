import time

from wtforms import StringField, PasswordField, Form, IntegerField
from wtforms.validators import Length, Email, DataRequired, ValidationError

#校验注册信息
from app.model.student import Student


class StudentForm(Form):

    name = StringField('姓名', validators=[DataRequired(message='姓名不可以为空')])
    born = StringField('生日', validators=[DataRequired(message='学号不可以为空')])
    nation = StringField('民族', validators=[DataRequired(message='民族不可以为空')])
    address = StringField('地址', validators=[DataRequired(message='地址不可以为空')])
    idcard = StringField('身份证', validators=[DataRequired(message='身份证不可以为空')])
    classroom = StringField('班别', validators=[DataRequired(message='班别不可以为空')])
    number = StringField('学号', validators=[DataRequired(message='学号不可以为空')])
    profession = StringField('专业', validators=[DataRequired(message='专业不可以为空')])

    def validate_number(self,field):
        if Student.query.filter_by(number=field.data).first():
            raise ValidationError('新生已注册')
