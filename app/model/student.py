import time
from datetime import datetime

from sqlalchemy import Column, Integer, String

from app.model.base import Base


class Student(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    create_time = Column('create_time',Integer)#注册时间
    nation = Column(String(50), nullable=False)#民族
    born   =Column(Integer, nullable=False)#出生
    address =Column(String(256), nullable=False)#地址
    idcard =Column(String(128), nullable=False)#身份证
    classroom =Column(String(50), nullable=False)#班级
    number =Column(String(128), nullable=False)#学号
    profession =Column(String(128), nullable=False)#专业
    image = Column(String(1024))#照片

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())#获取当前时间，并以时间戳格式保存(即注册时间)









