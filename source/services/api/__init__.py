# coding: utf8
""" 
@File: __init__.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/11 2:35
"""

from flask import Blueprint
from flask_cors import CORS

Api = Blueprint(
    name='api',
    import_name=__name__,
    url_prefix='/api/private/v1'
)

CORS(app=Api, supports_credentials=True)
from source.services.api.views.DataAnalyse.BaseApi import *
from source.services.api.views.DataAnalyse.test import test
from source.services.api.views.DataAnalyse.AnalyseDataTime import *
from source.services.api.views.DataAnalyse.AnalyseDataScore import *
from source.services.api.views.DataAnalyse.AnalyseDataCountry import *

