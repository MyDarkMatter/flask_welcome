from flask import Flask
from app.model.base import db


def create_app():
    #实例化核心对象
    app = Flask(__name__)
    register_blueprint(app)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app


#注册蓝图路由
def register_blueprint(app):
    from app.api import api
    app.register_blueprint(api)