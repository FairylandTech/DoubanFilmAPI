# coding: utf8
""" 
@File: server.py
@Author: Alice(From Chengdu.China)
@HomePage: https://github.com/AliceEngineerPro
@CreatedTime: 2022/11/14 22:45
"""
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from source.services.core.CoreServer import app

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(52015)
IOLoop.instance().start()
