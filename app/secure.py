
#服务器配置
DEBUG = False

THREADED = True#启用多线程


#数据库配置
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:DNFdmc2013@localhost:3308/flask'
# 开启数据库查询性能测试
SQLALCHEMY_RECORD_QUERIES = True

# 性能测试的阀值
DATABASE_QUERY_TIMEOUT = 0.5

SQLALCHEMY_TRACK_MODIFICATIONS = True

WTF_CSRF_CHECK_DEFAULT = False

SQLALCHEMY_ECHO = True
SECRET_KEY = 'secret!'