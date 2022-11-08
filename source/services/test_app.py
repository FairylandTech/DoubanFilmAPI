# coding: utf8
""" 
@File: test_app.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/9 0:42
"""

from flask import Flask

app = Flask(import_name=__name__)

@app.route('/')
def index():
    return 'HelloWorld'


if __name__ == '__main__':
    app.run(debug=True)

