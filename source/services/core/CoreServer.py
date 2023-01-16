# coding: utf8
""" 
@File: CoreServer.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/9 0:42
"""
from flask import Flask, jsonify
from flask_cors import CORS
from settings import Config
from source.services.api import Api
from source.services.api.PublicApi import PublicApi
from flask_sqlalchemy import SQLAlchemy

app = Flask(
    import_name=__name__,
    template_folder='{}/templates'.format(Config.BASE_DIR),
    static_folder='{}/static'.format(Config.BASE_DIR),
)
app.config.from_object(Config.RUN_ENV)
db = SQLAlchemy(app)
# app.config['JSON_AS_ASCII'] = False 
CORS(app, supports_credentials=True)
public_api = PublicApi()


@app.route('/')
def root():
    return jsonify(public_api.get_build_response_json(code=200, msg='Successful'))


app.register_blueprint(blueprint=Api)


def run(debug: bool = False, host: str = '127.0.0.1', port: int = 5000):
    print(app.url_map)
    app.run(debug=debug, host=host, port=port)
