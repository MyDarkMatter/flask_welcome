import time
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy#flask插件必须要在总路由器中注册
from sqlalchemy import Column, Integer, SmallInteger, String

#子类Sub_SQLAlchemy继承父类SQLAlchemy
class SQLAlchemy(_SQLAlchemy):

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()  # 错误回滚
            raise e  # 抛异常
db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    name = Column(String(50), nullable=False)  # 姓名


    def set_attrs(self, attrs):
        for key, value in attrs.items():
            if hasattr(self, key) and key != 'id':#判断当前对象是否包含名字为key的属性
                if key == 'born':
                    print(value)
                    value = self.born_time(value)
                setattr(self, key, value)

    #生日转为时间戳
    def born_time(self,born):
        timeArray = time.strptime(born, "%Y-%m-%d %H:%M:%S")
        # 转换成时间戳
        return int(time.mktime(timeArray))