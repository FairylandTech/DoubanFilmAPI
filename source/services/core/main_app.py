# coding: utf8
""" 
@File: main_app.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/9 0:42
"""

from flask import Flask, redirect
from flask_cors import CORS
from settings import Config
import os
from source.services.home import Home
from source.services.home import views
from source.services.api import Api
from source.services.api.views import IndexApi
from source.services.api.views import PublicApi

app = Flask(
    import_name=__name__,
    template_folder='{}/templates'.format(Config.BASE_DIR),
    static_folder='{}/static'.format(Config.BASE_DIR),
)
app.config['JSON_AS_ASCII'] = False
CORS(app, supports_credentials=True)


@app.route('/')
def root():
    return redirect(location='/home/index')


app.register_blueprint(blueprint=Home)
app.register_blueprint(blueprint=Api)
print(app.url_map)


def run(debug: bool = False, host: str = '127.0.0.1', port: int = 5000):
    app.run(debug=debug, host=host, port=port)
