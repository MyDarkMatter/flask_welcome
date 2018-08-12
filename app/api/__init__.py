from flask import Blueprint
from flask_cors import CORS


#注册蓝图
api = Blueprint('api',__name__)

from app.api import register,video,register
