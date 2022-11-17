# coding: utf8
""" 
@File: __init__.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/11 1:29
"""

from flask import Blueprint
from flask_cors import CORS
from settings import Config

Home = Blueprint(
    name='home',
    import_name=__name__,
    url_prefix='/home',
    template_folder='{}/templates'.format(Config.BASE_DIR),
    static_folder='{}/static'.format(Config.BASE_DIR),
)

CORS(app=Home, supports_credentials=True)


